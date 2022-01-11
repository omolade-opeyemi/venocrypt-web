from django.urls import path
from . views import *

urlpatterns = [
    path('', encryptTextView, name='encrypt'),
    path('file.html', encryptFileView, name='encryptfile'),
    path('decrypt.html', decryptTextView, name='decrypt'),
    path('fdecrypt.html', decryptFileView, name='decryptfile' )
    
]
