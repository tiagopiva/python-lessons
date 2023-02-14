#In this assignment (given) you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
texto = open("C:/Users/tiago.belluomini/Desktop/Python/regex_texto_teste.txt")
texto = texto.read()
soma = None
y = re.findall('[0-9]+', texto)
for numero in y:
    numero = int(numero)
    if soma is None: 
        soma = numero
    elif soma is not None:
        soma = soma + numero
        
print(soma)