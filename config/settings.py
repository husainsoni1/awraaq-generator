from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'dev-awraaq-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'editor.apps.EditorConfig',
    "django_ckeditor_5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
            ]
        },
    }
]

WSGI_APPLICATION = 'config.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_5_CONFIGS = {
    "default": {
        "language": {
            "content": "ar"
        },
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "|",
            "fontFamily", "fontSize", "|",
            "link", "bulletedList", "numberedList", "|",
            "outdent", "indent", "|",
            "blockQuote", "insertTable", "|",
            "undo", "redo",
        ],
        "fontFamily": {
            "options": [
                "default",
                "AlKanz",
                "KanzAlMarjaan",
                "Arial",
                "Times New Roman",
            ],
            "supportAllValues": True
        }
    }
}

CKEDITOR_5_DEFAULT_CONFIG = "default"

# Use BigAutoField for primary keys
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SQLite database for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),
    }
}