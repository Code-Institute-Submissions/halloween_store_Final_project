"""
Django settings for hc project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u(0#i!3$82q$*g!_^q7^i4n^zk-25***p4k65420=%@c1t$i-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'stripe',
    'crispy_forms',
    'widget_tweaks',
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

ROOT_URLCONF = 'hc.urls'

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
                'store.context_processors.menu_links',
                'store.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'hc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}


DATABASES = {
    'default': dj_database_url.parse('postgres://ytroinyvvidqmb:4cc2151c1ad382b04f8553e1f013d54bddddf2746f8eb309da69850f066fc530@ec2-54-247-79-178.eu-west-1.compute.amazonaws.com:5432/d68tofssre50uh')

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

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
STRIPE_PUBLISHABLE_KEY = 'pk_test_51HhHTOFLDz0n3wg9PCaMqzbCN9ktATSKKexfhyoPdg5CgLLPSY0mt1ivjhy0w93n1YymoOdvqXE9ejT13VSTVl8d00uL4kUnum'
STRIPE_SECRET_KEY = 'sk_test_51HhHTOFLDz0n3wg9IwuoJOMUiWBw1TZYNLdavVG0HKexqWi5fFJCeTlr13z2OAPxxcf0AdE7Yn3QMlkDSatq3QM300jypdiPzo' 
CRISPY_TEMPLATE_PACK = 'bootstrap4'


EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= "smtp.gmail.com"
EMAIL_HOST_USER= "thehalloweenstore@gmail.com"
EMAIL_HOST_PASSWORD= "password"
EMAIL_PORT= 587
EMAIL_USE_TLS= True
DEFAULT_FROM_EMAIL= "thehalloweenstore@gmail.com"