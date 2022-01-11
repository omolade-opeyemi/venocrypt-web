from django.shortcuts import render, redirect

from .import File
from . import Password
from . import Text
from .forms import encryptForm
import os
from django.core.files.storage import FileSystemStorage
import mimetypes
from django.http import HttpResponse

def encryptTextView(request):
    if request.method == 'POST':
        password = request.POST['password']
        text = request.POST['text']
        key = Password.getKey(password)
        result = Text.encryptt(key,text)
        return render(request, 'encrypt.html', {'result':result})

    form = encryptForm()
    context={'form':form}
    return render(request, 'encrypt.html')

def encryptFileView(request):
    if request.method == 'POST':
        password = request.POST['password']
        fileObj = request.FILES['file']
        output = request.POST['output']
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
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition']='attachment; filename=%s' % filename
        return response
    return render(request, 'encrypt.html')

def decryptTextView(request):
    if request.method == 'POST':
        password = request.POST['password']
        text = request.POST['text']
        key = Password.getKey(password) 
        result = Text.decryptt(key, text)
        return render(request, 'decrypt.html', {'result':result})

    return render(request, 'decrypt.html')

def decryptFileView(request):
    if request.method == 'POST':
        password = request.POST['password']
        fileObj = request.FILES['file']
        output = request.POST['output']
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
    return render(request, 'decrypt.html')
