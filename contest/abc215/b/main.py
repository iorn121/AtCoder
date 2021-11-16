N = int(input())
k = 0
while pow(2, k) <= N:
    k += 1

print(k-1)
