from wei.settings.common import *
from dotenv import load_dotenv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DEV_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# load environment variables from .env file
load_dotenv()

# get the values for AZURE_STORAGE_CONNECTION_STRING and AZURE_STORAGE_CONTAINER_NAME
AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
AZURE_STORAGE_CONTAINER_NAME = os.environ.get('AZURE_STORAGE_CONTAINER_NAME')

# get the values for AZURE_TABLE_STORAGE_CONNECTION_STRING and AZURE_TABLE_STORAGE_TABLE_NAME
AZURE_TABLE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_TABLE_STORAGE_CONNECTION_STRING')
AZURE_TABLE_STORAGE_TABLE_NAME = os.environ.get('AZURE_TABLE_STORAGE_TABLE_NAME')