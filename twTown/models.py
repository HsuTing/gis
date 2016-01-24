from __future__ import unicode_literals

from django.contrib.gis.db import models

class TwTown(models.Model):
    townsn = models.CharField(max_length=13)
    townid = models.CharField(max_length=12)
    countyname = models.CharField(max_length=8)
    townname = models.CharField(max_length=8)
    name = models.CharField(max_length=12)
    geom = models.GeometryField(srid=4326)

    def __str__(self):
        return self.name
