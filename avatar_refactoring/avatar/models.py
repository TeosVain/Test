from django.db import models

from .utils import resize_avatar


class Avatar(models.Model):
    image = models.ImageField(upload_to='avatars/')
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if self.image and not hasattr(self.image.file, 'processed'):
            processed = resize_avatar(self.image, self.name)
            self.image.save(processed.name, processed, save=False)
            self.image.file.processed = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name