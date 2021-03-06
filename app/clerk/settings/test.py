from . import *

SUBMISSION_EMAILS = ["test@example.com"]

DEBUG = False
EMAIL_PREFIX = "TEST"
SECRET_KEY = "test-secret-key"
ALLOWED_HOSTS = ["*"]
DATABASES["default"]["name"] = "test"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_ROOT = os.path.join(BASE_DIR, "test_media")


# Django-q cluster should run synchronously
Q_CLUSTER = {
    "name": "clerk",
    "sync": True,  # tasks run in sync
    "timeout": 60,  # seconds,
    "retry": 60,  # seconds,
    "save_limit": 250,  # number of tasks saved to broker
    "orm": "default",  # Use Django's ORM + database for broker
}
