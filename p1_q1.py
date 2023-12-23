#Prova 01 - 31/10/23

numero = int(input())
soma = 0
contador = 1
divisor = 0
while contador <= numero:
    divisor = numero % contador
    if divisor == 0:
        soma = soma + contador

    contador += 1
print(soma)