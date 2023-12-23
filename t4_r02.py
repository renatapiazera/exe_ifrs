inscritos = int(input())
c = 1
votosCarlos = int(input())
while c < inscritos:
    votos = int(input())
    c += 1
if votos > votosCarlos:
    print('N')
else:
    print('S')
