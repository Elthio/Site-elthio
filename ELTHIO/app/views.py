from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status
import app.urls as app


# Create your views here.

@api_view(['GET'])
def hello(request):

    """
        This function return all router valid!!
    """

    if request.method == 'GET':

        list_app = [app]
        urlpatterns_list = []
        
        for apk in list_app:
            for pattern in apk.urlpatterns:

                if apk == app:
                    apk = '/'
                
                route = f"{str(apk)}" + str(pattern.pattern) 
                urlpatterns_list.append(route)
            
        return Response(urlpatterns_list)