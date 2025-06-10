from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1234567890'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'board',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

MIDDLEWARE = []
ROOT_URLCONF = 'boardproject.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'boardproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'