import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from fastapi import UploadFile


class EmailSender:
    def __init__(self, smtp_host: str, smtp_port: int, email: str, password: str):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_email(
        self,
        recipient: str,
        subject: str,
        html_body: str,
        attachments: list[UploadFile] | None = None,
    ):
        print('Estableciendo conexión con el servidor SMTP...')
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as smtp:
            smtp.starttls()
            print('Autenticando...')
            smtp.login(self.email, self.password)
            print('Autenticado exitosamente.')

            message = MIMEMultipart()
            message['From'] = self.email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(html_body, 'html'))

            # Adjuntos (UploadFile)
            if attachments:
                for upload_file in attachments:
                    file_content = upload_file.file.read()
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file_content)
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename="{upload_file.filename}"',
                    )
                    message.attach(part)

            print('Enviando correo...')
            smtp.sendmail(self.email, recipient, message.as_string())
            print('Correo enviado correctamente.')
