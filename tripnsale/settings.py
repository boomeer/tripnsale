"""
Django settings for tripnsale project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ug0dk251ba6te45^%0qjyna$47kh^6o@!0_5%*@7zel4^6uhv2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

ALLOWED_HOSTS = ["tripnsale.com", "127.0.0.1"]

CURRENT_HOST = "tripnsale.com"


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'offer',
    'user',
    'util',
    'place',
    'gallery',
    'guarant',
    'infos',
    'valute',
    'mail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tripnsale.urls'

WSGI_APPLICATION = 'tripnsale.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tripnsale.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    "static",
)


STATIC_ROOT = "/var/www/tripnsale/static/"

TEMPLATE_DIRS = (
    "templates",
)


MEDIA_ROOT = "/var/www/tripnsale/upl/"

MEDIA_URL = "/upl/"

EMAIL_SENDER_MAIL = "admin@tripnsale.com"
EMAIL_SENDER_NAME = "Trip & Sale"

ENABLE_ACTIVATION = True

EMAIL_DKIM_DOMAIN = None
EMAIL_DKIM_SELECTOR = "info"

# Use this structure in priv_settings (!!!!!) to make a pair with keys
# DO NOT WRITE THE KEYS TO THE MAIN settings.py!
class _EmailKeys:
    def __init__(self, priv, pub, fromFiles=False):
        if fromFiles:
            with open(priv, 'r') as f:
                self.private = priv.read()
            with open(pub, 'r') as f:
                self.public = pub.read()
        else:
            self.private = priv
            self.public = pub
EMAIL_DKIM_KEYS = None

if os.path.isfile(os.path.join(BASE_DIR, "tripnsale", "priv_settings.py")):
    from tripnsale.priv_settings import *
