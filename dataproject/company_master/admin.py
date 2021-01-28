from django.contrib import admin
from company_master.models import CompanyData
# Register your models here.


def change_class(modeladmin, request, queryset):
    '''
    Change company class using actions option
    '''
    queryset.update(COMPANY_CLASS='Private')


change_class.short_description = "Mark selected companies as Private"


@admin.register(CompanyData)
class CompanyDataAdmin(admin.ModelAdmin):
    """
    Coustomize admin interface
    """
    list_display = [
        "COMPANY_NAME",
        "COMPANY_CLASS",
        "COMPANY_STATUS",
        "AUTHORIZED_CAP",
        "DATE_OF_REGISTRATION"
        ]

    list_filter = ("BUSINESS_ACTIVITY", "COMPANY_CLASS", "COMPANY_STATUS")
    ordering = ['DATE_OF_REGISTRATION']
    search_fields = ['COMPANY_NAME']
    actions = [change_class]
