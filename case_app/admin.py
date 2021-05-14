from django.contrib import admin

# Register your models here.
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'case_number',
        'case_title',
        'court_name',
        'ruling_type',
        'case_type',
        'issue_category',
        )

    list_filter = (
        'court_name',
        'ruling_type',
        'case_type',
        'issue_category',
    )

admin.site.register(Case, CaseAdmin)