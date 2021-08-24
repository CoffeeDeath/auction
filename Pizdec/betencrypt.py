# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:42:40 2021

@author: user
"""
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
def session_key_text_send(public_key,bet):
    sessionkey = Random.new().read(32)
    iv = Random.new().read(16)
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    ciphertext = iv + obj.encrypt(bet)
    cipherrsa = PKCS1_OAEP.new(public_key)
    sessionkey = cipherrsa.encrypt(sessionkey)
    return [sessionkey, ciphertext]
