# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from twCounty.models import TwCounty

def output(request, countysn):
    data = serialize('geojson', TwCounty.objects.filter(countysn=countysn))
    return JsonResponse(json.loads(data), safe=False)

def total(request):
    data = serialize('geojson', TwCounty.objects.all())
    return JsonResponse(json.loads(data), safe=False)
