from __future__ import unicode_literals

from django.contrib.gis.db import models

class TwVillage(models.Model):
    villagesn = models.CharField(max_length=14)
    villageid = models.CharField(max_length=15)
    countyname = models.CharField(max_length=8)
    townname = models.CharField(max_length=8)
    villagenam = models.CharField(max_length=8)
    name = models.CharField(max_length=16)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.name
