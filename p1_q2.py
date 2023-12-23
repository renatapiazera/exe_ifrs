#Prova 01 - 31/10/23

grupo = int(input())
c = 0
if grupo > 66:
    print('-')
else:
    if grupo < 9:
        a = grupo % 5
        if a == 0:
            print('0 -',1)
        else:
            print('0 -',2)
    else:
        a = grupo // 9
        resto_a = grupo % 9
        if resto_a == 0:
            print(a,'- 0')
        else:
            b = resto_a //5
            resto_b = resto_a % 5
            if resto_b == 0:
                print(a, '-', b)
            else:
                print(a, '-', b+1)