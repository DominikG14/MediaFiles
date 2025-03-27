from django.http import HttpRequest
from django.shortcuts import render, redirect
from utils.views import get_template
from . import urls, forms, models


def upload(request: HttpRequest):
    template = get_template(app=urls.app_name)

    if request.method == 'GET':
        form = forms.UploadMediaForm()

    if request.method == 'POST':
        form = forms.UploadMediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = forms.UploadMediaForm()

    return render(request, template, {
        'form': form,
    })


def display_all(request: HttpRequest):
    template = get_template(app=urls.app_name)

    media_files = models.MediaFile.objects.all()

    return render(request, template, {
        'media_files': media_files,
    })