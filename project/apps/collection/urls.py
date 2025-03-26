from django.urls import path
from . import views, redirects


app_name = 'collection'
urlpatterns = []


PATHS = [
    path('upload/', views.upload, name='upload'),
    path('display/all', views.display_all, name='display_all'),
]

REDIRECTS = [

]


urlpatterns += PATHS
urlpatterns += REDIRECTS