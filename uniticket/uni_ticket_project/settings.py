import os
import pathlib

from .settingslocal import *
from django_form_builder.settings import *
from uni_ticket_bootstrap_italia_template.settings import *


HOME_PAGE = "/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
DATA_DIR = os.path.join(BASE_DIR, "data")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(DATA_DIR, "static")
if not os.path.exists(STATIC_ROOT):
    pathlib.Path(STATIC_ROOT).mkdir(parents=True, exist_ok=True)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")
if not os.path.exists(MEDIA_ROOT):
    pathlib.Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)

# used for pdf creation and other temporary files
CACHE_DIR = "uni_ticket_project_cache"
TMP_DIR = os.path.sep.join((BASE_DIR, CACHE_DIR, "tmp"))
if not os.path.exists(TMP_DIR):
    pathlib.Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if "djangosaml2" in INSTALLED_APPS:
    MIDDLEWARE.append("djangosaml2.middleware.SamlSessionMiddleware")

ROOT_URLCONF = "uni_ticket_project.urls"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

WSGI_APPLICATION = "uni_ticket_project.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
USE_I18N = True
USE_TZ = True

# from django 3.2
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# SECURITY
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
