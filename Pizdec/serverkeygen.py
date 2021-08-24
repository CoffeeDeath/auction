# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:14:24 2021

@author: user
"""
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
def server_key_gen():
    privatekey = RSA.generate(2048)
    publickey = privatekey.publickey()
    return [privatekey, publickey] 
