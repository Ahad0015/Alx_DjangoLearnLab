"""
Django settings for tm_api project.
"""

from pathlib import Path

# Base directory (two levels up from here)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key-change-in-prod"
DEBUG = True   
ALLOWED_HOSTS = []   # maybe ['127.0.0.1', 'localhost']?

INSTALLED_APPS = [
    # Default Django stuff
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3rd party packages
    "rest_framework",
    "django_filters",

    # Local apps
    "api",
    "tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "corsheaders.middleware.CorsMiddleware",  # if I bring CORS in
]

ROOT_URLCONF = "tm_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # could add BASE_DIR / "templates" later
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tm_api.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # probably fine unless I move to Postgres
    }
}

# Skipping password validators for now, kinda annoying in dev
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Addis_Ababa"   # my local timezone
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]  # maybe later

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework config (using JWTs)
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
}

# Login/logout redirects for the HTML views
LOGIN_REDIRECT_URL = "task_list"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"




