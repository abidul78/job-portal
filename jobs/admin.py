from django.contrib import admin

from .models import Application, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company_name',
        'location',
        'salary',
        'posted_by',
        'date_posted',
    )
    search_fields = ('title', 'company_name')
    list_filter = ('location', 'date_posted')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status', 'date_applied')
    list_filter = ('status', 'date_applied')
    search_fields = ('applicant__username', 'job__title')
