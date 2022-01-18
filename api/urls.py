from django.urls import path
from . views import *

urlpatterns = [
    path('encryptText', EncryptText.as_view()),
    path('encryptFile', EncryptFile.as_view()),
    path('decryptText', DecryptText.as_view()),
    path('decryptFile', DecryptFile.as_view()),   
]
