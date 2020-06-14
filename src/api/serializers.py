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

    def create(self, validated_data):
        print(validated_data)
        attendance_status_data = validated_data.pop('attendancestatus_set')
        data = Attendance.objects.create(**validated_data)
        for attendance_status in attendance_status_data:
            AttendanceStatus.objects.create(
                attendance=data,
                status=attendance_status.get('status'),
                student=attendance_status.get('student')
            )
        return data
