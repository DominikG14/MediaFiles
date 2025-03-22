from django import forms
from django.conf import settings
from .models import MediaFile
from categories.models import Category
from datetime import datetime
import uuid
import os


class UploadMediaForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['file']
        labels = {}
    
    def save(self, commit: bool = True):
        media: MediaFile = super().save(commit=False)

        media.title, media.extension = os.path.splitext(media.file.name)
        media.file_size = media.file.size

        media.extension = media.extension[1:].upper()
        if media.extension == 'MP4':
            media.is_video = True

        if MediaFile.objects.filter(file__contains=media.file.name).exists():
            media.status = MediaFile.Status.DUPLICATED
            media.title = f'{media.title}-{uuid.uuid4().hex}'

            duplicates, created = Category.objects.get_or_create(name=settings.DUPLICATES_DIR)
            media.category = duplicates
        else:
            no_category, created = Category.objects.get_or_create(name=settings.NO_CATEGORY_DIR)
            media.category = no_category

        if commit:
            media.save()
            metadata = media.get_metadata()

            if metadata['DateTime'] is not None:
                media.created_at = metadata['DateTime']
                media.creation_year = media.created_at.year
            
            if media.is_video and metadata['Duration'] is not None:
                media.duration = metadata['Duration']
            media.save()

        return media