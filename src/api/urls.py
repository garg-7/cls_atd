from django.urls import path
from .views import Image

urlpatterns = [
    path('image/', Image.as_view(), name='upload-image'),
]