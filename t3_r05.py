contador = 0
num = int(input())
while num != 0:
    """if 100 <= num <= 200:"""
    if num >= 100 and num <= 200:
        contador += 1
    num = int(input())
print(contador)
