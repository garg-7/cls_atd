from django.contrib import admin
from .models import LegalDecisions, LegalScholarship, Faq


def approve(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.register(LegalDecisions)
class LegalDecisionsAdmin(admin.ModelAdmin):
    list_display = ['court_name', 'country', 'email_address', 'is_approved']
    list_filter = ['country', 'is_approved']
    actions = [approve]


@admin.register(LegalScholarship)
class LegalScholarshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'email_address', 'is_approved']
    list_filter = ['country', 'is_approved']
    actions = [approve]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass
