nc = int(input("NUMERO DE CANDIDATOS: "))
cont = 1
maior = 0

if (nc > 1):
    NotaCarlos = int(input("VOTOS: "))
    while (cont < nc):
        nota = int(input("VOTOS: "))
        if (nota > maior):
            maior == nota
        cont += 1
    if (maior > NotaCarlos):
        print("N")
    else:
        print("S")

else:
    print("NÚMERO DE CANDIDATOS INVÁLIDO!")