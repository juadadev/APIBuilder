from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.email_notification_routes import email_router

app = FastAPI(
    title='API de notificaciones',
    description='API para notificaciones de pagos por algún medio de comunicación, Ejemplo: WhatsApp, SMS, Email.',
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(email_router, prefix='/api')
