N = int(input())
S = input()
W = list(map(int, input().split()))
pair = []
for i in range(N):
    w = W[i]
    s = 1 if S[i] == "0" else -1
    pair.append((w, s))
pair.sort()
start = S.count("1")
ans = start
for w, s in pair:
    start += s
    ans = max(ans, start)

print(ans)
