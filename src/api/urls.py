from django.urls import path
from .views import Image, AttendanceAPIView, StudentAPIView


urlpatterns = [
    path('image/', Image.as_view(), name='upload-image'),
    path('attendance/', AttendanceAPIView.as_view(), name='attendance'),
    path('students/', StudentAPIView.as_view(), name='students')
]
