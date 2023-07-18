from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from home.api.serializers import (
                                    CategorySerial, 
                                    CategorySerial2, 
                                    StoryCreatSerial,
                                    StorySerial
                                    )
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from home.models import Category, Story
import json


def test(request):
    # students = [{'name':'cavid'}, {'name':'aysel'}]
    # return HttpResponse(json.dumps(students), content_type='application/json')
    category = []
    data = Category.objects.all()
    for i in data:
        category.append({'name':i.name, 'slug':i.slug, 'image':i.image.url})

    return JsonResponse(category, safe=False)

@api_view(['GET', 'POST'])
def category_view(request):
    if request.method == 'POST':
        data = request.data
        serial = CategorySerial(data = data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data)

    data = Category.objects.all()
    serial = CategorySerial(data, many = True, context = {'request':request})
    return Response(data=serial.data)

@api_view(['GET'])
def category_view_id(request, id):
    # data = Category.objects.get(id = id)
    data = get_object_or_404(Category, id = id)
    serial = CategorySerial(data, context = {'request':request})
    return Response(data=serial.data)

class StoryView(APIView):
    def get(self, request):
        data = Story.objects.all()
        serail = StorySerial(data, many = True)
        return Response(data = serail.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serial = StoryCreatSerial(data = data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data, status=status.HTTP_201_CREATED)
        return Response(data={'errors':serial.errors})
    
class StoryViewSlug(APIView):
    def get(self, request, slug):
        data = Story.objects.get(slug = slug)
        serial = StorySerial(data, context = {'request':request})
        return Response(data = serial.data, status=status.HTTP_200_OK)
