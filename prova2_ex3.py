quanti = int(input("QUANTAS TEMPERATURAS: "))
contador = 0
menor = 0
maior = 0
while contador < quanti:
    temperatura = int(input("TEMPERATURA: "))
    if quanti == 1:
        print(temperatura,"/",temperatura)
        exit()
    else:
        if temperatura <= menor:
            menor = temperatura
        if temperatura > maior:
            maior = temperatura
    contador += 1
print(menor, maior)
