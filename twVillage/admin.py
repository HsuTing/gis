from django.contrib.gis import admin
from models import TwVillage

class TwVillageAdmin(admin.ModelAdmin):
    list_display = ('villagesn',
    'villageid',
    'countyname',
    'townname',
    'villagenam',
    'name')
admin.site.register(TwVillage, TwVillageAdmin)
