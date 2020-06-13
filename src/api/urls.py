from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import Image, AttendanceViewSet

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('image/', Image.as_view(), name='upload-image'),
]

urlpatterns += router.urls
