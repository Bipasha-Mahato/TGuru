"""
Django settings for tribeGuru project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k-=5)(7z1@m75oyuyc)dny=d5xlb@8tnid*r8=t=w94yai&_nj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['203.110.240.164', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'school.apps.SchoolConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'entCell.apps.EntcellConfig',
    'embed_video',
    'vAssist.apps.VassistConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tribeGuru.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'tribeGuru.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'users_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users.db.sqlite3',
    },
    'school_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'school.db.sqlite3',
    },
    'media_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'media.db.sqlite3',
    },
    'entCell_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'entCell.db.sqlite3',
    },
    'vAssist_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'vAssist.db.sqlite3',
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
DATABASE_ROUTERS = ['routers.db_routers.AuthRouter','routers.db_routers.School','routers.db_routers.Media', 'routers.db_routers.EntCell', 'routers.db_routers.vAssist',]
# Added Manually

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'tribeguru-home'
LOGIN_URL = 'login'

# /*to define the connectivities*/
