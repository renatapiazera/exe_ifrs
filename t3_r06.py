arvoreA = int(input())
alturaAnoA = int(input())
arvoreB = int(input())
alturaAnoB = int(input())
tempo = int(input())
contador = 0
"""fazer o teste do nunca antes"""
if arvoreB < arvoreA and alturaAnoB < alturaAnoA:
    print('Nunca')
    if arvoreA < arvoreB and alturaAnoA < alturaAnoB:
        print('Nunca')
else:
    while contador < tempo:
        arvoreA = arvoreA + alturaAnoA
        arvoreB = arvoreB + alturaAnoB
        contador += 1
        if arvoreA < arvoreB:
            print(arvoreB, arvoreA)
        if arvoreA > arvoreB:
            print(arvoreA, arvoreB)

    print(tempo)
