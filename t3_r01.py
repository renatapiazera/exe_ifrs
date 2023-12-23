n = int(input())
c = 1
qd = 0
while c <= n:
    d = n % c
    if d == 0:
        qd += 1
    c += 1
if qd == 2:
    print('É Primo!')
else:
    print('Não é Primo!')
