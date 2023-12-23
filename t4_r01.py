testes = int(input())
premio = 0
contador = 0

while (contador < testes):
    porta = int(input())
    if (porta != 1):
        premio += 1
    contador += 1
print(premio)
