from Crypto.Cipher import AES
from Crypto import Random
import os
from django.core.files.storage import FileSystemStorage

def encrypt(key, fileObj,output):
    chunksize = 64 * 1024

    x=fileObj.name
    y=x.replace(' ','')
    fs= FileSystemStorage()
    filePath=fs.save(y,fileObj)
    filePath=fs.url(filePath)

    ext = y.split('.')[-1]
    outputFile ='./media/'+ output +'.'+ext
    
    filesize = str(os.path.getsize('.'+filePath)).zfill(16)
    
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open('.'+filePath, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def decrypt(key,fileObj,output):
    chunksize = 64 * 1024

    x=fileObj.name
    y=x.replace(' ','')
    fs= FileSystemStorage()
    filePath=fs.save(y,fileObj)
    filePath=fs.url(filePath)

    ext = y.split('.')[-1]
    outputFile ='./media/'+ output +'.'+ext

    with open('.'+filePath, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)