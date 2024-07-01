from math import sin, cos, pi
def is_in_here(x, y, z, r):
    if (x + 3) ** 2 + (y + 3) ** 2 + (z + 3) ** 2 < (r / 3) ** 2:
        return 0
    return int(x ** 2 + y ** 2 + z ** 2 < r ** 2)

def update_field(a, b, c, cnt):
    t = False
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if min(a[i][j],b[i][k],c[j][k]) % 2 != is_in_here(i + 0.5 - len(a) / 2, j + 0.5 - len(a) / 2, k + 0.5 - len(a) / 2, len(a) / 2):
                    a[i][j] = cnt
                    b[i][k] = cnt
                    c[j][k] = cnt
                    t = True
    return a, b, c, t

n = 30
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
c = [[0] * n for i in range(n)]
t = True
cnt = 0
while t:
    cnt += 1
    a, b, c, t = update_field(a, b, c, cnt)
if (a != c):
    print("\033[1mLEFT:\033[0m")
    for i in a:
        for j in i:
            if j <= 7:
                print(end = "\033[4" + str(j) + "m  \033[0m")
        print()
    print()
print("\033[1mUP:\033[0m")
for i in b:
    for j in i:
        if j <= 7:
            print(end = "\033[4" + str(j) + "m  \033[0m")
        else:
            print("ERROR")
    print()
print()
if (a != c):
    print("\033[1mFRONT:\033[0m")
    for i in c:
        for j in i:
            if j <= 7:
                print(end = "\033[4" + str(j) + "m  \033[0m")
        print()
    print()
