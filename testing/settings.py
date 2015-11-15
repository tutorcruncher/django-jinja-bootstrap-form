import os
BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = 'django-jinja-bootstrap-form'

TEMPLATE_DEBUG = DEBUG = False

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'bootstrapform_jinja',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testapp.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

import django
if django.get_version().startswith('1.8'):
    TEMPLATES = [
        {
            'BACKEND': 'django_jinja.backend.Jinja2',
            'APP_DIRS': True,
            'DIRS': TEMPLATE_DIRS,
            'OPTIONS': {
                'match_extension': '.jinja',
                'trim_blocks': True,
                'lstrip_blocks': True,
            }
        },
    ]
else:
    TEMPLATE_LOADERS = (
        'django_jinja.loaders.FileSystemLoader',
        'django_jinja.loaders.AppLoader'
    )
