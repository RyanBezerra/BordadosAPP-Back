import os
from pathlib import Path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'dTxjsltTHyUTKSQrcsxhrZUyGSdzXFTy',
        'HOST': 'junction.proxy.rlwy.net',
        'PORT': '11815',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',  # sua aplicação
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # adicione isso
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # apenas para desenvolvimento 