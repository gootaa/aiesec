from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aiesec',
        'USER': 'postgres',
        'PASSWORD': 'ammg1998',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]