import environ
from .base import *

env = environ.Env(
    DOMAINS=(str, '.docker.localhost')
)

DATABASES = {
    'default': env.db_url()
}


SESSION_COOKIE_DOMAIN = env('DOMAINS')
SESSION_COOKIE_SAMESITE = None

DEBUG = False