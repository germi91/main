import ed25519

# Cargar claves
private_key_hex = open("Practica\ed25519-priv", "rb").read()
public_key_hex = open("Practica\ed25519-publ", "rb").read()

private_key = ed25519.SigningKey(private_key_hex)
public_key = ed25519.VerifyingKey(public_key_hex)

# Mensaje a firmar
message = 'El equipo está preparado para seguir con el proceso, necesitaremos más recursos.'

# Convertir el mensaje a bytes
message_bytes = message.encode('utf-8')

# Calcular la firma
signature = private_key.sign(message_bytes)

# Verificar la firma
try:
    public_key.verify(signature, message_bytes)
    print("La firma es válida")
except ed25519.BadSignatureError:
    print("La firma no es válida")

# Imprimir la firma en hexadecimal
print("Firma en hexadecimal:", signature.hex())