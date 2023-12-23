#Prova 01 - 31/10/23

quantasTemp = int(input())
c = 0
t = 0
while c < quantasTemp:
    temperatura = int(input())

    if quantasTemp == 1:
        print(t ,'/' ,t)
    else:
        temperatura = t

        if t > temperatura:
            maior = t
        else:
            menor = t
        c += 1



print(menor)