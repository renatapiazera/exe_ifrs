pessoas = int(input())
carro9 = 0
carro5 = 0
if pessoas <= 66:
    if pessoas < 36:
        carro9 = 4
        resto = pessoas - 36
        if resto % 5 == 0:
            carro5 = resto // 5
        else:
            carro5 = resto // 5 + 1
    else:
        carro9 = pessoas // 9
        pessoas %= 9
        if pessoas > 5:
            carro9 += 1
        else:
            carro5 += 1
    print(carro9,'-',carro5)
else:
    print('-')

