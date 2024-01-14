from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import SHA256

# La Clave AES proporcionada por el enunciado
clave_aes = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

# Se calcula el SHA-256
hash_sha256 = SHA256.new(data=clave_aes)
kcv_sha256 = hash_sha256.digest()[:3]

print("KCV(SHA-256):", kcv_sha256.hex())

# Creamos un bloque de 16 bytes de ceros
bloque_ceros = bytes(16)

# Creamos un IV de ceros
iv_ceros = bytes(16)

# Iniciamos el cifrado AES
cipher = AES.new(key=clave_aes, mode=AES.MODE_CBC, iv=iv_ceros)

# Ciframos el bloque de ceros
cifrado = cipher.encrypt(pad(bloque_ceros, 16))

# Obtenemos los primeros 3 bytes del resultado
kcv_aes = cifrado[:3]

print("KCV(AES):", kcv_aes.hex())