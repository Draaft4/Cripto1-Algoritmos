#ord -> Transformar de char a ascii
#chr -> Transformar de ascii a char


cadenaTexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

clave = "vigenre"
lenClave = len(clave)

actual = 0

encriptado = ""

for i in cadenaTexto:
    if(actual<lenClave):
        ascii = ord(i)
        if(ascii > 64 and ascii < 90) :
            #Codigo para mayusculas
            posicion = ascii - 65
            valClave =  clave[actual]
            posicionClave = ord(valClave) - 97
            suma = posicion + posicionClave
            if(suma > 25):
                suma = suma - 25
            nuevoVal = suma + 65
            encriptado = encriptado + chr(nuevoVal)
        else:
            if(ascii > 96 and ascii < 123):
                #Codigo para minusculas
                posicion = ascii - 97
                valClave =  clave[actual]
                posicionClave = ord(valClave) - 97
                suma = posicion + posicionClave
                if(suma > 25):
                    suma = suma - 25
                nuevoVal = suma + 97
                encriptado = encriptado + chr(nuevoVal)
            else:
                encriptado = encriptado + " "
        actual = actual + 1
    else:
        actual = 0
print(encriptado)
