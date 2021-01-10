from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']  # 이후 고정 아이피 등록하기
SITE_URL = ''

# Prod Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# AWS S3
AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'static.projectt1.shop'
# ex)static.abcde.io

AWS_S3_CUSTOM_DOMAIN = 's3.%s.amazonaws.com/%s' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)

AWS_S3_FILE_OVERWRITE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
AWS_S3_SECURE_URLS = False

STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# AWS_S3_CUSTOM_DOMAIN = '%s' % AWS_STORAGE_BUCKET_NAME # 이건 Router53 연결 이후
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# media
DEFAULT_FILE_STORAGE = 'config.s3media.MediaStorage'