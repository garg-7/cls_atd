from rest_framework import serializers
from .models import Attendance, AttendanceStatus


class AttendanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatus
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    status = AttendanceStatusSerializer(many=True)

    class Meta:
        model = Attendance
        fields = '__all__'
