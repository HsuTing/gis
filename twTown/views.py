# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

from twTown.models import TwTown

def output(request, townsn):
    data = serialize('geojson', TwTown.objects.filter(townsn=townsn))
    return JsonResponse(json.loads(data), safe=False)

def total(request):
    data = serialize('geojson', TwTown.objects.all())
    return JsonResponse(json.loads(data), safe=False)
