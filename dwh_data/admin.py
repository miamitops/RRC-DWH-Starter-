from django.contrib import admin
from dwh_data.models import BaseData, BDGroup, BDCOOAddress, BDCOAAddress, BDVulnerability
admin.site.register(BaseData)
admin.site.register(BDGroup)
admin.site.register(BDCOOAddress)
admin.site.register(BDCOAAddress)
admin.site.register(BDVulnerability)
# Register your models here.
