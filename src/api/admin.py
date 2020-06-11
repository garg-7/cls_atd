from django.contrib import admin
from .models import Student, Attendance, AttendanceStatus


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model = Student
        fields = '__all__'


class AttendanceStatusInline(admin.StackedInline):
    model = AttendanceStatus


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    inlines = (AttendanceStatusInline, )

    class Meta:
        model = Attendance
        fields = '__all__'
