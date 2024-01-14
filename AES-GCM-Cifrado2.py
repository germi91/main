from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64decode
import base64

# Datos proporcionados
clave_hex = 'E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74'
nonce_original = '9Yccn/f5nJJhAt2S'
texto_original = 'He descubierto el error y no volveré a hacerlo mal'

# Convertir la clave y el nonce de b64 a bytes
clave = bytes.fromhex(clave_hex)
nonce_bytes = b64decode(nonce_original)

# El cifrado AES/GCM
cipher = AES.new(key=clave, mode=AES.MODE_GCM, nonce=nonce_bytes)

# Convertir el texto a bytes y cifrarlo
texto_bytes = bytes(texto_original, 'utf-8')
texto_cifrado_bytes = cipher.encrypt(texto_bytes)

# Obtener el tag de autenticación
tag = cipher.digest()

# Presentar el resultado en hexadecimal y en base64
texto_cifrado_hex = texto_cifrado_bytes.hex()
texto_cifrado_base64 = base64.b64encode(texto_cifrado_bytes).decode()

print(f"Texto cifrado en hexadecimal: {texto_cifrado_hex}")
print(f"Texto cifrado en base64: {texto_cifrado_base64}")