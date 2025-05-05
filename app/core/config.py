import os

from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class Config:
    _instance: Optional['Config'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        self.SMTP_EMAIL = os.getenv('SMTP_EMAIL', '')
        self.SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
        self.SMTP_HOST = os.getenv('SMTP_HOST', '')
        self.SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
