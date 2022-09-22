S = list(input())
Q = int(input())
convert = {"A": 0, "B": 1, "C": 2}
convert2 = ["A", "B", "C"]
for _ in range(Q):
    t, k = map(int, input().split())
    cnt = t % 3
    k -= 1
    for i in range(t):
        cnt += (k >> i) & 1
        if k < 2**i:
            break
    index = (convert[S[k >> t]]+cnt) % 3
    print(convert2[index])
