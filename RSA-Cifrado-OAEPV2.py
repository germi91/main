from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import os
my_path = os.path.abspath(os.getcwd())

fichero_pub = my_path + "\Practica\clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())




mensaje = bytes.fromhex("af3c29921ff79af39de3bf8032bcf7e2a4c3136ef3520dcf48a246537cc4ecc1")

encryptor = PKCS1_OAEP.new(keypub,SHA256)
encrypted = encryptor.encrypt(mensaje)

print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")