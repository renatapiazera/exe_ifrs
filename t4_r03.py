numCaixas = int(input())
contador = 0
cred = 100
while contador < numCaixas:
    valorCaixas = int(input())
    saldo = (cred + valorCaixas)
    cred = saldo
    contador +=1
if cred <= 100:
    print("100")
else:
     print(cred)