from django.urls import path
from . import views, redirects


app_name = 'collection'
urlpatterns = []


PATHS = [
    path('upload/', views.upload, name='upload'),
    path('test/', views.test),
]

REDIRECTS = [

]


urlpatterns += PATHS
urlpatterns += REDIRECTS