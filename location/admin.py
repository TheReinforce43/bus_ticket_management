from django.contrib import admin

from location.Model.location_model import ServiceDistrictModel

@admin.register(ServiceDistrictModel)
class ServiceDistrictAdmin(admin.ModelAdmin):
    list_display = ('districtName', 'division', 'responsiblePerson', 'created_at', 'updated_at')
    search_fields = ('districtName', 'division', 'responsiblePerson__username')
    list_filter = ('division', 'created_at', 'updated_at')
    ordering = ('-created_at',) 
