from mongoengine import Document, StringField, DateTimeField, URLField
from django.utils.text import slugify
from datetime import datetime

class Post(Document):
    title = StringField(max_length=200, required=True)
    slug = StringField(unique=True)
    content = StringField()
    image_url = URLField()
    created_at = DateTimeField(default=datetime.utcnow)  # 👈 auto-set current time

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
