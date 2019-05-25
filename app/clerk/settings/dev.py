# flake8: noqa
from . import *

DEBUG = True
SECRET_KEY = 'its-a-secret-key!'

MATT_EMAIL = 'matt@anikalegal.com'
SUBMISSION_EMAILS = [MATT_EMAIL]

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(https?://)?(localhost|127\.0\.0\.1|0\.0\.0\.0)(:\d{4})?$',
)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'anika-clerk-test'
AWS_S3_CUSTOM_DOMAIN = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {'level': 'INFO', 'handlers': ['console']},
    'handlers': {'console': {'level': 'INFO', 'class': 'logging.StreamHandler'}},
    'loggers': {
        'reader': {'handlers': ['console'], 'level': 'INFO', 'propagate': True},
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': True},
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
