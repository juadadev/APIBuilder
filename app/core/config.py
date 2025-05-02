import os

from typing import cast

from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = cast(str, os.getenv('SMTP_EMAIL'))
SMTP_PASSWORD = cast(str, os.getenv('SMTP_PASSWORD'))
SMTP_HOST = cast(str, os.getenv('SMTP_HOST'))
SMTP_PORT = cast(int, os.getenv('SMTP_PORT'))
