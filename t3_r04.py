fiboA = 0
fiboB = 1
sequenciaFibo = 0
primeiroValor = int(input())
segundoValor = int(input())

while sequenciaFibo < primeiroValor:
    sequenciaFibo = fiboB+fiboA
    fiboA = fiboB
    fiboB = sequenciaFibo

while sequenciaFibo <= segundoValor:
    print(sequenciaFibo)
    if sequenciaFibo == 1:
        print(sequenciaFibo)
    sequenciaFibo = fiboB+fiboA
    fiboA = fiboB
    fiboB = sequenciaFibo
