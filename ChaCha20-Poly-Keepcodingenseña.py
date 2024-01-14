from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

try:
    textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'utf-8')
    clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
    nonce_original = "9Yccn/f5nJJhAt2S"
    nonce_bytes = b64decode(nonce_original + "==")[:12]

    datos_asociados = bytes('', 'utf-8')
    
    # Cifrado con ChaCha20-Poly1305
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_bytes)
    cipher.update(datos_asociados)
    texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoPlano)

    # Imprimir resultados
    print("Nonce:", nonce_bytes.hex())
    print("Criptograma:", texto_cifrado_bytes.hex())
    print("MAC:", tag.hex())

except (ValueError, KeyError) as error:
    print("Problemas al cifrar...")
    print("El motivo del error es:", error)