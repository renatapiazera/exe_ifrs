num = int(input())
sdiv = 0
c = 1
while c < num:
    d = num % c
    if d == 0:
        sdiv += c
    c += 1
if sdiv == num:
    print('É Perfeito!')
else:
    print('Não é Perfeito!')
