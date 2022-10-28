import onetimepad
inicial = "7803572110014e2e54031a"

print("Texto a desencriptar = ", inicial)

clave = "0l;@"

print("Clave = ", clave)

cifrado = onetimepad.decrypt(inicial, clave)

print("Clave encriptada = ", cifrado)