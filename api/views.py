from rest_framework.views import APIView
from rest_framework.response import Response
from venom import *
import os
import mimetypes
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import FileSerializer,TextSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status


class EncryptText(GenericAPIView):
    serializer_class=TextSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            text = serializer.validated_data.get('text')
            key = Password.getKey(password)
            result = Text.encryptt(key,text)
            message = repr(result)
            return Response({'message':result})
        else:
            return Response(serializer.errors, status=400 )


class DecryptText(GenericAPIView):
    serializer_class=TextSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            text = serializer.validated_data.get('text')
            key = Password.getKey(password)
            result = Text.decryptt(key, text)
            return Response({'message':result})
        else:
            return Response(serializer.errors, status=400 )


class EncryptFile(GenericAPIView):
    serializer_class = FileSerializer
    parser_classes = (FormParser, MultiPartParser)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            fileObj = serializer.validated_data.get('file')
            output = serializer.validated_data.get('outputName')
            key = Password.getKey(password)
            File.encrypt(key, fileObj, output)
            listOfFiles=os.listdir('./media/')
            x=fileObj.name
            y=x.replace(' ','')
            ext = y.split('.')[-1]
            fl_path = './media/' +output +'.'+ext
            filename = str(fl_path.split('/')[-1])
            fl = open(fl_path, 'rb')
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl,  content_type=mime_type)
            response['Content-Disposition']='attachment; filename=%s' % filename
            return response  
        else:
            return Response(serializer.errors, status=400 )

class DecryptFile(GenericAPIView):
    serializer_class = FileSerializer
    parser_classes = (FormParser, MultiPartParser)
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            fileObj = serializer.validated_data.get('file')
            output = serializer.validated_data.get('outputName')
            key = Password.getKey(password)
            File.decrypt(key, fileObj, output)
            listOfFiles=os.listdir('./media/')
            x=fileObj.name
            y=x.replace(' ','')
            ext = y.split('.')[-1]
            fl_path = './media/' +output +'.'+ext
            filename = str(fl_path.split('/')[-1])
            fl = open(fl_path, 'rb')
            mime_type, _ = mimetypes.guess_type(fl_path)
            response = HttpResponse(fl, content_type=mime_type)
            response['Content-Disposition']='attachment; filename=%s' % filename
            return response
            
        else:
            return Response(serializer.errors, status=400 )



# Create your views here.
