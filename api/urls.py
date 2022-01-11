from django.urls import path
from . views import *

urlpatterns = [
    #path('', encryptTextView, name='encrypt'),
    path('swagger', File.as_view()),
    #path('decrypt.html', decryptTextView, name='decrypt'),
    #path('fdecrypt.html', decryptFileView, name='decryptfile' )   
]
