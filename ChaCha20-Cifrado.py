from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'utf-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_original = "9Yccn/f5nJJhAt2S"
nonce_bytes = b64decode(nonce_original + "==")[:12]

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave, nonce=nonce_bytes)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())

