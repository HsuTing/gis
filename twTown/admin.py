from django.contrib.gis import admin
from models import TwTown

class TwTownAdmin(admin.ModelAdmin):
    list_display = ('townsn',
###    'townid',
###    'countyname',
###    'townname',
    'name')
admin.site.register(TwTown, TwTownAdmin)
