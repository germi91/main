from Crypto.Hash import HMAC, SHA256


#Generamos el hmac, en este caso SHA512 - HMAC-512
#c096860be238d7e0a6d3929c7ba06f468d3e6b7b28132ba48d553f845788c513004b1ec78758f24e9e1f006ae9a89651f80023f5505927a7aecd6529fa12c081
key=bytes.fromhex("A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB")
mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida","utf8")
hmac256 = HMAC.new(key,mensaje_bytes,digestmod=SHA256)

#Propio de los hmac, como representar el valor
print(hmac256.hexdigest())

