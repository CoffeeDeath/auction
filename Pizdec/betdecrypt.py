# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:08:37 2021

@author: user
"""
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
def bet_decrypt(private_key, sessionkey, ciphertext):
    cipherrsa = PKCS1_OAEP.new(privatekey)
    sessionkey = cipherrsa.decrypt(sessionkey)
    iv = ciphertext[:16]
    obj = AES.new(sessionkey, AES.MODE_CFB, iv)
    bet = obj.decrypt(ciphertext)
    bet = bet[16:]
    return bet