import random
import secrets
from Crypto.Hash import SHA256
import bcrypt

def salt():
    return secrets.randbits(16)

def bsalt(a):
    hashed = bcrypt.hashpw(a.encode('utf-8'),bcrypt.gensalt())
    return hashed

def sha(b):
    hasher = SHA256.new(b.encode('utf-8'))
    return hasher.digest()


def getKey(password):
    key = sha(password)
    return key

