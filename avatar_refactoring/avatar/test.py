import io
import boto3
from PIL import Image
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from avatar.models import Avatar
from django.conf import settings


class AvatarUploadTest(TestCase):
    def setUp(self):
        '''Set up a test avatar image and calculate its original size.'''
        img = Image.new('RGB', (1000, 800), color='blue')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        self.original_size = buffer.tell()
        buffer.seek(0)

        self.upload_file = SimpleUploadedFile(
            "test.jpg",
            buffer.read(),
            content_type="image/jpeg"
        )


    def test_avatar_processed_and_uploaded(self):
        '''Test that the avatar is processed and uploaded to S3 with reduced size.'''
        avatar = Avatar.objects.create(image=self.upload_file, name='Test')
        s3 = boto3.client(
            's3',
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        obj = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=f'media/{avatar.image.name}')
        content = obj['Body'].read()
        self.assertLess(len(content), self.original_size)
        img = Image.open(io.BytesIO(content))
        self.assertEqual(img.size[0], img.size[1])