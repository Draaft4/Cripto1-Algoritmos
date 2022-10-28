#ord -> Transformar de char a ascii
#chr -> Transformar de ascii a char

cadenaTexto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

k = 7
N = len(cadenaTexto)
print("N = ",N)
encriptada = ""
for i in cadenaTexto:
    ascii = ord(i)
    if((ascii > 64 and ascii < 90)or(ascii > 96 and ascii < 123)):
        nuevo_valor = (ascii + k)
        encriptada = encriptada + chr(nuevo_valor)
    else:
        encriptada = encriptada + " "

print(encriptada)
