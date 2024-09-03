# GENERADOR DE CONTRASEÑAS 
# LA LONGITUD ES PROPORCIONADA POR EL USUARIO

import string
import random

longitud = int(input("Ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es: "+ contraseña)

