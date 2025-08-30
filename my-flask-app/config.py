import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "clave_dev_segura")
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPOLNY = True,
    SESSION_COOKIE_SAMESITE = 'Lax'
