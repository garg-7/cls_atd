from django.urls import path
from .views import Image, AttendanceAPIView


urlpatterns = [
    path('image/', Image.as_view(), name='upload-image'),
    path('attendance/', AttendanceAPIView.as_view(), name='attendance')
]
