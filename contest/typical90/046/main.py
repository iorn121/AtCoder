N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a = [0]*46
b = [0]*46
c = [0]*46

for x in A:
    a[x % 46] += 1
for x in B:
    b[x % 46] += 1
for x in C:
    c[x % 46] += 1

ans = 0
for x, na in enumerate(a):
    for y, nb in enumerate(b):
        for z, nc in enumerate(c):
            if (x+y+z) % 46 == 0:
                ans += na*nb*nc
print(ans)
