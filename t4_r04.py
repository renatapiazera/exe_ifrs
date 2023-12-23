"""= 0"""
dormirSintervalo = int(input())
duracaoVoo = int(input())
numRefeicoes = int(input())
contador = 0
t = 0
while contador < numRefeicoes:
    yi = int(input())
    tempoDormir = yi - dormirSintervalo
    contador += 1
    if tempoDormir >= dormirSintervalo and tempoDormir > 0:
        t += 1
if t < 1 or numRefeicoes == 0:
    print("N")
else:
    print("Y")
