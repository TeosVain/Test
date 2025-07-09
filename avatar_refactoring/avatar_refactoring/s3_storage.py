import boto3
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    bucket_name = 'teos-avatar-bucket'
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = 'teos-avatar-bucket'
    location = 'static'


def generate_presigned_url(object_key, expires_in=3600):
    s3 = boto3.client(
        's3',
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    key = 'media/' + object_key
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': key
        },
        ExpiresIn=expires_in
    )
    return url
