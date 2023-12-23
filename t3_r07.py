primeiroNumero = int(input())
ultimoNumero = int(input())
contador = 0
numero = 0
numeroAleatorio = 1
while numeroAleatorio != 0:
    numeroAleatorio = int(input())
    if numeroAleatorio >= primeiroNumero and numeroAleatorio <= ultimoNumero:
        contador += 1


print(contador)
