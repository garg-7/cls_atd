from django.urls import path
from .views import HomeView, AttendanceView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('attendance', AttendanceView.as_view(), name='attendance')
]
