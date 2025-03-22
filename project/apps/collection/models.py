from django.db import models
from django.conf import settings

from categories.models import Category

from PIL import Image, ExifTags
from pymediainfo import MediaInfo
from datetime import datetime
import os


class MediaFile(models.Model):
    class Status(models.IntegerChoices):
        TRACKED = 0, 'TRACKED'
        LOST = 1, 'LOST'
        DUPLICATED = 2, 'DUPLICATED'

    def upload_to(instance, filename: str) -> str:
        return os.path.join(settings.MEDIA_ROOT, instance.category.name, filename)
    
    # File storage
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_to)
    status = models.PositiveIntegerField(choices=Status, default=Status.TRACKED)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True, blank=True)
    is_video = models.BooleanField(default=False)

    # Metadata
    created_at = models.DateTimeField(null=True, blank=True)
    creation_year = models.PositiveIntegerField(null=True, blank=True)
    extension = models.CharField(max_length=10)
    file_size = models.PositiveIntegerField(null=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    # Timestamps
    uploaded_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):      
        return super().save(*args, **kwargs)
        
    def get_metadata(self) -> dict:
        if self.is_video:
            return self.__get_video_metadata()
        return self.__get_image_metadata()
        
    def __get_image_metadata(self) -> dict:
        with Image.open(self.file.path) as img:
            exif_data = img._getexif()

        if exif_data is None:
            return {'DateTime': None}

        exif_readable = {ExifTags.TAGS.get(tag, tag): value for tag, value in exif_data.items()}
        return {
            'DateTime': datetime.strptime(exif_readable['DateTime'], '%Y:%m:%d %H:%M:%S')
        }
    
    def __get_video_metadata(self) -> dict:
        media_info = MediaInfo.parse(self.file.path)
        
        for track in media_info.tracks:
            if track.track_type == 'General':
                return {
                    'DateTime': track.recorded_date,
                    'Duration': track.duration / 1000
                }

    def __str__(self):
        return f'{self.category.name} - {self.title}'