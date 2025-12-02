#Crear codigo
import secrets
#
import string


def crear_codigo(size=6, chars=string.ascii_uppercase + string.digits):
    codigo = []
    for i in range(size):
        codigo.append(secrets.choice(chars))
    return "".join(codigo)