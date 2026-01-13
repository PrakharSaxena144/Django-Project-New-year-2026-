# Prakhar -----> Prakhar@0612

from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model= ChaiReview
    extra= 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'date_added')
    inlines= [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display= ('name', 'location')
    filter_horizontal= ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display= ('certificate_number', 'chai', 'issue_date', 'valid_until')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)