from itertools import product
N, K = map(int, input().split())
T = []
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)

junretsu = list(product(range(K), repeat=N))
flg = True

for x in junretsu:
    check = 0
    for i, num in enumerate(x):
        check ^= T[i][num]
    if check == 0:
        flg = False

print("Nothing" if flg else "Found")
