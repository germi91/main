import jwt

# Token proporcionado
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"

# Clave secreta
secreto = "secreto"

try:
    # Decodificar el JWT
    decode_jwt = jwt.decode(token, secreto, algorithms="HS256")
    print(decode_jwt)
except jwt.ExpiredSignatureError:
    print("Token expirado")
except jwt.InvalidTokenError:
    print("Token inválido")