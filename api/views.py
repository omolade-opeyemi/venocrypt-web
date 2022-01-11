from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import YourSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class File(APIView):
    
      
    password=openapi.Parameter('password', in_=openapi.IN_QUERY, description='Descript', type=openapi.TYPE_STRING)
    file=openapi.Parameter('file', in_=openapi.IN_QUERY, description='Descript', type=openapi.TYPE_FILE)
    # @swagger_auto_schema (manual_parameters=([file])
    # @swagger_auto_schema(manual_parameters=[password])
    
    def post(self, request):
        serializers = YourSerializer
        
        password = request.GET.get['password']
        file = request.FILES['file']
        print(password, file)
        return Response({"message: file accepted"}, status=200)



# Create your views here.
