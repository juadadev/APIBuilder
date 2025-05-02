import os
import shutil

from fastapi import UploadFile

from app.schemas.email_request import EmailRequest
from app.schemas.priority import Priority

from ...interface.iemail_notification_builder import IEmailNotificationBuilder


class EmailNotificationBuilderDirector:
    def __init__(self, builder: IEmailNotificationBuilder):
        self._builder = builder
        self.upload_dir = 'temp_uploads'
        os.makedirs(self.upload_dir, exist_ok=True)

    def construct_minimal_email(self, email_request: EmailRequest):
        processed_attachments = self._process_attachments(email_request.attachments)
        return (
            self._builder.set_to(email_request.to)
            .set_subject('¡Tu pago ha sido aprobado!')
            .set_body(
                f'Pago por ${email_request.amount:.2f} con {email_request.payment_method.value} confirmado. NOTIFICACION: {email_request.notification_type.value}'
            )
            .set_attachments(processed_attachments)
            .set_priority(Priority.ALTA)
            .build()
        )

    def _ensure_upload_dir_exists(self):
        """Asegura que el directorio de upload existe con los permisos correctos"""
        try:
            os.makedirs(self.upload_dir, exist_ok=True)
            # Asegurar permisos (opcional, dependiendo de tu entorno)
            os.chmod(self.upload_dir, 0o755)
        except OSError as e:
            raise RuntimeError(f'No se pudo crear el directorio de uploads: {e}') from e

    def _save_upload_file(self, file: UploadFile) -> str:
        """Guarda un archivo subido y devuelve su ruta"""
        try:
            if not file.filename:
                raise ValueError('El archivo subido no tiene nombre')

            # Asegurar que el directorio existe (doble verificación)
            self._ensure_upload_dir_exists()

            safe_filename = self._sanitize_filename(file.filename)
            file_path = os.path.join(self.upload_dir, safe_filename)

            # Guardar el archivo de manera atómica
            temp_path = f'{file_path}.tmp'
            with open(temp_path, 'wb') as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Renombrar para operación atómica
            os.rename(temp_path, file_path)

            return file_path
        except Exception as e:
            # Limpiar archivo temporal si hubo error
            if 'temp_path' in locals() and os.path.exists(temp_path):
                os.remove(temp_path)
            raise RuntimeError(f'Error al guardar archivo: {e}') from e

    @staticmethod
    def _sanitize_filename(filename: str) -> str:
        """Sanitiza el nombre del archivo para seguridad
        Args:
            filename: Nombre del archivo (garantizado que no es None)
        Returns:
            str: Nombre del archivo sanitizado
        """
        # Caracteres permitidos: alfanuméricos, puntos, guiones bajos, guiones
        allowed_chars = (' ', '.', '_', '-')
        return ''.join(c for c in filename if c.isalnum() or c in allowed_chars).strip()

    def cleanup_attachments(self, attachment_paths: list[str]):
        """Elimina archivos temporales después de enviar el email"""
        for path in attachment_paths:
            try:
                if path and os.path.exists(path):
                    os.remove(path)
            except OSError as e:
                print(f'Error al eliminar archivo temporal {path}: {e}')

    def _process_attachments(self, attachments: list[UploadFile] | None) -> list[str]:
        if not attachments:
            return []

        processed: list[str] = []
        for attachment in attachments:
            if isinstance(attachment, UploadFile) and attachment.filename:
                file_path = self._save_upload_file(attachment)
                processed.append(file_path)  # guarda ruta real del archivo
            else:
                print(f'Archivo inválido o no reconocido: {attachment}')
        return processed
