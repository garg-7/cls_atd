from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.roll_no


class Attendance(models.Model):
    date = models.DateField(unique_for_date=True, auto_now_add=True)
    status = models.ManyToManyField(Student, through='AttendanceStatus',
                                    through_fields=('attendance', 'student'))

    def __str__(self):
        return self.date


class AttendanceStatus(models.Model):
    STATUS_CHOICES = (
        ('1', 'PRESENT'),
        ('2', 'ABSENT')
    )

    attendance = models.ForeignKey(Attendance, models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return self.student

