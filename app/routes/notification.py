from fastapi import APIRouter, HTTPException
from ..domain.builder.sms_notification_builder import SMSNotificationBuilder
from ..domain.builder.whatsapp_notification_builder import WhatsappNotificationBuilder
from ..domain.builder.director.sms_notification_builder_director import (
    SMSNotificationBuilderDirector,
)
from ..domain.builder.director.whatsapp_notication_builder_director import (
    WhatsAppNotificationBuilderDirector,
)

# importa tus builders/directores según organización
from ..schemas.notification_request import NotificationRequest

router = APIRouter()


@router.post("/notificaciones/")
def crear_notificacion(request: NotificationRequest):
    if request.channel == "sms":
        builder = SMSNotificationBuilder()
        director = SMSNotificationBuilderDirector(builder)
        notification = director.construct_sms_notification(
            phone_number=request.phone_number,
            amount=request.amount,
            payment_method=request.payment_method,
        )

    elif request.channel == "whatsapp":
        builder = WhatsappNotificationBuilder()
        director = WhatsAppNotificationBuilderDirector(builder)
        notification = director.construct_whatsapp_notification(
            amount=request.amount,
            payment_method=request.payment_method,
            phone_number=request.phone_number,
            message=request.message,
            media_url=request.media_url,
            caption=request.caption,
            interactive_buttons=request.interactive_buttons,
            language=request.language,
        )

    else:
        raise HTTPException(status_code=400, detail="Canal no soportado")

    # Aquí enviarías la notificación
    # notification.send()  <-- si implementaste esa interfaz
    return {"mensaje": "Notificación construida y enviada con éxito"}
