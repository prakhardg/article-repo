from django.shortcuts import render, get_object_or_404
from django.core import serializers
from .models import Article
from django.http import HttpResponse

from django.views.generic import View


# Create your views here.

def show_data_json(request, id):
    # print("here")
    instance = get_object_or_404(Article, id=id)
    # if instance is not None:
    #     print(instance.title)
    try:
        json = serializers.serialize('json', [instance,])
    except Exception as e:
        print(e)
    return HttpResponse(json)
