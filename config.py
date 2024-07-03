import os
import secrets

SECRET_KEY = '7eab1cb58c02267cb46f2f124e903640'

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', SECRET_KEY)
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '7421212211:AAH2-g3HC56z3OKdH0DzVnHwHr3qEgFf74E')