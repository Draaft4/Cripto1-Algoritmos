import onetimepad
inicial = "Hola mundo!"

print("Texto a encriptar = ", inicial)

clave = "0l;@"

print("Clave = ", clave)

cifrado = onetimepad.encrypt(inicial, clave)

print("Clave encriptada = ", cifrado)