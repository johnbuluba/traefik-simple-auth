import environ
from .base import *

env = environ.Env()

DATABASES = {
    'default': env.db_url()
}


SESSION_COOKIE_DOMAIN = ".docker.localhost"
SESSION_COOKIE_SAMESITE = None

DEBUG = False