from fastapi import FastAPI

from .routes.email_notification_routes import email_router
from .routes.sms_notification_routes import sms_router

app = FastAPI(
    title="API de notificaciones",
    description="API para notificaciones de pagos por algún medio de comunicación, Ejemplo: WhatsApp, SMS, Email.",
)

app.include_router(email_router, prefix="/api")
app.include_router(sms_router, prefix="/api")
