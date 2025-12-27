#=== ▼この2行を追加▼ ===
import os
import dj_database_url

from .common import *

DEBUG = False

ALLOWED_HOSTS = ["*", ]  # === 追加 ===

# ▼▼▼ 追加 ▼▼▼

AWS_STORAGE_BUCKET_NAME = "recipe-post-app"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL
# ▲▲▲ 追加ここまで ▲▲▲

#=== ▼▼▼ここから追加▼▼▼ ===
DATABASES = {
    'default': dj_database_url.config()
}
#=== ▲▲▲ここまで追加▲▲▲ ===
