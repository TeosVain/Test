from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def resize_avatar(image_field, name, size=(300, 300), format='JPEG', quality=85):
    img = Image.open(image_field)
    if format.upper() == 'JPEG' and img.mode != 'RGB':
        img = img.convert('RGB')
    min_side = min(img.size)
    left = (img.width - min_side) // 2
    top = (img.height - min_side) // 2
    img = img.crop((left, top, left + min_side, top + min_side))
    if img.width > size[0]:
        img = img.resize(size, Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format=format, quality=quality)
    content_file = ContentFile(buffer.getvalue())
    content_file.name = f'{name}.jpeg'
    return content_file
