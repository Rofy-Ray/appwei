from wei.settings.common import *
from dotenv import load_dotenv

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE= True