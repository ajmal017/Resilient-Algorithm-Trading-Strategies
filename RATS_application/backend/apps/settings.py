"""
Django settings for RATS_application project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import apps as backend_apps
from django.core.exceptions import ImproperlyConfigured
import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RATS_BACKEND_DIR = os.path.dirname(backend_apps.__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y9)j7ftq*#70$teyq194*!zg%ta%^uet4*(5(s=t&1@3z8uhsa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://127.0.0.1:8000', 'http://127.0.0.1:8083', 'localhost', '127.0.0.1', 'tealinux.com', 'localrats.com']

# Load the configuration files. This gives the django project flexibility so
# that it can run in other environments (local, remote) seamlessly, with all
# the differences and specifics for each environment being handled in the
# config file.
RATS_CONFIG_FILE_PATH = os.path.join(RATS_BACKEND_DIR,
                                     'RATS.conf')
if not os.path.exists(RATS_CONFIG_FILE_PATH):
    raise ImproperlyConfigured("Failed to locate configuration file. Expected "
                               "path: {}".format(RATS_CONFIG_FILE_PATH))
CONFIG = configparser.ConfigParser(allow_no_value=True)
CONFIG.read(RATS_CONFIG_FILE_PATH)

BASE_URL = CONFIG['settings']['base_url']
BASE_URL_SERVICES = CONFIG['settings']['base_url_services']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',


    # Apps
    'apps.home',
    'apps.quant_connect',
    'apps.oauth2',
    'apps.cred',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': CONFIG['database']['name'],
        'USER': CONFIG['database']['user'],
        'PASSWORD': CONFIG['database']['password'],
        'HOST': CONFIG['database']['host'],
        'PORT': CONFIG['database']['port']
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#CORS_ORIGIN_ALLOW_ALL = True
#SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_SAMESITE=None
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_SSL_REDIRECT = False
CORS_ORIGIN_ALLOW_ALL = True 
CORS_ALLOW_CREDENTIALS = True