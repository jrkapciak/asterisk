from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

INSTALLED_APPS += ["debug_toolbar", "drf_yasg"]
ROOT_URLCONF = "config.urls_dev"
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]  # nosec

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
    "SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}},
}
