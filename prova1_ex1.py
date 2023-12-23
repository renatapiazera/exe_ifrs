d1 = int(input())
m1 = int(input())
d2 = int(input())
m2 = int(input())
if m2 > m1:
    print(d1, '/', m1, ' - ', d2, '/', m2)
else:
    if m2 == m1:
        if d2 >= d1:
            print(d1, '/', m1, ' - ', d2, '/', m2)
        else:
            print(d2, '/', m1, ' - ', d1, '/', m2)
    else:
        print(d2, '/', m2, ' - ', d1, '/', m1)
