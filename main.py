# Oscar Fernando López Barrios
# Carné 20679

import jwt

# Funcion para codificar el JWT
def encode_jwt(payload, key):
    encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
    return encoded_jwt

# Funcion para codificar el jwt
def decode_jwt(encoded_jwt, key):
    try:
        decoded_payload = jwt.decode(encoded_jwt, key, algorithms=["HS256"])
        return decoded_payload
    except:
        print("Existe un ERROR con el JWT")

if __name__ == "__main__":
    # Payload y key de ejemplo
    payload = {'username': 'racso', 'id': 1624}
    key = 'racso12345'

    encoded_jwt = encode_jwt(payload, key)
    print("JWT codificado:", encoded_jwt)

    decoded_jwt = decode_jwt(encoded_jwt, key)
    print("Resultado de la decodificación:", decoded_jwt)
