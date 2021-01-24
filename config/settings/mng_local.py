from .mng import *

DEBUG = True
SITE_URL = 'http://127.0.0.1:8109'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret('LOCAL_DB_NAME'),
        'USER': get_secret('LOCAL_DB_USER'),
        'PASSWORD': get_secret('LOCAL_DB_PASSWORD'),
        'HOST': get_secret('LOCAL_DB_HOST'),
        'PORT': get_secret('LOCAL_DB_PORT'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
