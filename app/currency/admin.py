from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder
from import_export.admin import ImportExportModelAdmin

from currency.models import Rate, ContactUs, Source


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'source',
        'currency_type',
        'created'
    )
    list_filter = (
        'currency_type',
        ('created', DateRangeFilterBuilder())
    )
    search_fields = (
        'id',
        'buy',
        'source'
    )
    # readonly_fields = (
    #     'buy',
    #     'sell'
    # )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name',
        'created'
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'body'
    )
    list_filter = (
        'email_from',
        'subject'
    )
    search_fields = (
        'id',
        'subject',
        'body'
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
