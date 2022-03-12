V = list(map(int, input().split()))

ans = ["F", "M", "T"]

while V[0]>=0:
    for i in range(3):
        V[0] -= V[i+1]
        if V[0] < 0:
            print(ans[i])
            break
