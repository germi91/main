import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Clave proporcionada
clave = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')

# IV del ejercicio
iv_desc_bytes = bytes.fromhex('00' * 16)

# Texto cifrado del ejercicio
texto_cifrado_bytes = b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")

# Configurar el cifrador
cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)

try:
    # Descifrar el texto cifrado con relleno x923
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style='x923')

    # Imprimir el resultado
    print("Texto descifrado en hexadecimal:", mensaje_des_bytes.hex())
    print("Texto descifrado en UTF-8:", mensaje_des_bytes.decode("utf-8"))

except ValueError as error:
    print('Problemas para descifrar con relleno x923....')
    print("El motivo del error es:", error)