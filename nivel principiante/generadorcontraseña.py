import random 
#from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "1234567890"
simbolos = "!@#$%&()+=/"

base = minus + mayus + numeros + simbolos
longitud = 12

for _ in range(100):

    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    print (password)