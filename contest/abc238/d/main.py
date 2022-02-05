N = int(input())

for i in range(N):
    a, s = map(int, input().split())
    tmp = s-a*2
    if tmp < 0:
        print("No")
        continue
    flg = True
    for j in range(len(bin(a))):
        if (a >> j) & 1:
            if(tmp >> j) & 1 == 1:
                flg = False
    print("Yes" if flg else "No")
