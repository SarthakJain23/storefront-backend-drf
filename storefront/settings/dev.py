from .common import *


DEBUG = True

SECRET_KEY = "django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "care.Fi@123",
    }
}

CELERY_BROKER_URL = "redis://localhost:6379/1"


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

EMAIL_HOST = "localhost"
EMAIL_PORT = 2525
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
