"""
Django settings for yixiu project.

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
SECRET_KEY = 'e$-^vvyp$g47!zp9vvqpt*)c(lw2u^nrqqdez0&yuzszsn7g5*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    '/var/www/yixiu/static/templates/',
    '/Users/wangsong/Desktop/temp/myownpage/static/templates/',
)


ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'information',
    'blog',
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

ROOT_URLCONF = 'yixiu.urls'

WSGI_APPLICATION = 'yixiu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
mysql_name = 'wangsong'
mysql_user = 'root'
mysql_pass = ''
mysql_host = ''
mysql_host_s = ''
mysql_port = ''


DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': mysql_name,                      # Or path to database file if using sqlite3.
        'USER': mysql_user,                      # Not used with sqlite3.
        'PASSWORD': mysql_pass,                  # Not used with sqlite3.
        'HOST': mysql_host,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': mysql_port,                      # Set to empty string for default. Not used with sqlite3.
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
