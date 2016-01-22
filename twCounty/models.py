from __future__ import unicode_literals

from django.contrib.gis.db import models

class TwCounty(models.Model):
    countysn = models.CharField(max_length=13)
    countyname = models.CharField(max_length=8)
    name = models.CharField(max_length=8)
    geom = models.GeometryField()

    def __str__(self):
        return self.name
