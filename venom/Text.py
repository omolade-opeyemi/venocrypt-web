from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
import ast

def encryptt(key,text):
    message = text.encode('utf-8')
    IV = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded = pad(message, AES.block_size)
    ciphertext = cipher.encrypt(padded)
    crypted = IV + ciphertext
    print(crypted)
    s = str(crypted)[1: ]
    print(s)
    return s

def decryptt(key, text):
    message = text
    s = 'b'+message
    eval = ast.literal_eval(s)
    iv = eval[ :AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plainttext = unpad(cipher.decrypt(eval[AES.block_size : ]), AES.block_size)
    return plainttext.decode()

