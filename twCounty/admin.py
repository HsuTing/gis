from django.contrib.gis import admin
from models import TwCounty

class TwCountyAdmin(admin.ModelAdmin):
    list_display = ('countysn',
    'countyname',
    'name')
admin.site.register(TwCounty, TwCountyAdmin)
