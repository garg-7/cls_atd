from rest_framework import serializers
from .models import Attendance, AttendanceStatus


class AttendanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatus
        fields = ('status', 'student')


class AttendanceSerializer(serializers.ModelSerializer):
    attendance = AttendanceStatusSerializer(source='attendancestatus_set', many=True)

    class Meta:
        model = Attendance
        fields = ('date', 'attendance')
