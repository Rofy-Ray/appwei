from wei.settings.common import *
from dotenv import load_dotenv

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['appwei.azurewebsites.net']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# load environment variables from application settings
load_dotenv()

# get the values for AZURE_STORAGE_CONNECTION_STRING and AZURE_STORAGE_CONTAINER_NAME
AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
AZURE_STORAGE_CONTAINER_NAME = os.environ.get('AZURE_STORAGE_CONTAINER_NAME')

# get the values for AZURE_TABLE_STORAGE_CONNECTION_STRING and AZURE_TABLE_STORAGE_TABLE_NAME
AZURE_TABLE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_TABLE_STORAGE_CONNECTION_STRING')
AZURE_TABLE_STORAGE_TABLE_NAME = os.environ.get('AZURE_TABLE_STORAGE_TABLE_NAME')

STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage')

CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net']