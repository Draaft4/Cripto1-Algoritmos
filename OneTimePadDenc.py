import onetimepad
inicial = "78035721780b16420d060d"

print("Texto a desencriptar = ", inicial)

clave = "0l;@Xfc,ii,"

print("Clave = ", clave)

cifrado = onetimepad.decrypt(inicial, clave)

print("Clave desencriptada = ", cifrado)