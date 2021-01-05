def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def zakupy(x=0, y=0, z=0):
    A = 202
    B = 203
    C = 200
    K = 606
    w = nwd(A, B)
    print(f'w:{w}')
    return w + C / nwd(w, C) * K


zakupy()

# A*x+B*y+C*z = K -> nwd(A,B)*w +C*z = K
# A*x+B*x = nwd(A,B)*w
# nwd(A,B) = 1
# K = nwd(nwd(A,B),C) = nwd(1,200) = 1
# K = 1*w + C*z = nwd(nwd(A,B),C)
possible = []
suma = 606

a = 3
b = 2
c = 200

liczby = (a, b, c)

dzielniki = [int(suma / liczby[0]), int(suma / liczby[1]), int(suma / liczby[2])]
a = [single for single in range(dzielniki[0]+1)]
b = [single for single in range(dzielniki[1]+1)]
c = [single for single in range(dzielniki[2]+1)]

for aa in a:
    for bb in b:
        for cc in c:
            if liczby[0] * aa + liczby[1] * bb + liczby[2] * cc == suma:
                possible.append((aa, bb, cc))
print(possible)