# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from twVillage.models import TwVillage

def output(request, villagesn):
    data = serialize('geojson', TwVillage.objects.filter(villagesn=villagesn))
    return JsonResponse(json.loads(data), safe=False)

def total(request):
    data = serialize('geojson', TwVillage.objects.all())
    return JsonResponse(json.loads(data), safe=False)
