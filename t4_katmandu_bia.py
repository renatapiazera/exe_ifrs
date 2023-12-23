
t = int(input())
d = int(input())
m = int(input())
c = 1
soma = 0
while c < m:
    yi = int(input())
    if (yi - t) >= 1:
        soma += 1
    c += 1
    if c == m:
        yifinal = int(input())
        if (d - yifinal) >= t:
            soma += 1
if soma >= 1 or m == 0:
    print("Y")
else:
    print("N")
