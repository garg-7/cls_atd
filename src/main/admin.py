from django.contrib import admin
from .models import ClassImage


@admin.register(ClassImage)
class ClassImageAdmin(admin.ModelAdmin):
    pass
