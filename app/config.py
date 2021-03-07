import os
from dotenv import load_dotenv

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_PORT = os.getenv('MONGODB_PORT')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')
MESSAGE_QUEUE_NAME = os.getenv('MESSAGE_QUEUE_NAME')
MESSAGE_QUEUE_HOST = os.getenv('MESSAGE_QUEUE_HOST')
MESSAGE_QUEUE_USERNAME = os.getenv('MESSAGE_QUEUE_USERNAME')
MESSAGE_QUEUE_PASSWORD = os.getenv('MESSAGE_QUEUE_PASSWORD')
