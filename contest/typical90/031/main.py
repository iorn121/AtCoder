N = int(input())
W = map(int, input().split())
B = map(int, input().split())

dp = [[-1]*1326 for _ in range(51)]


def groudy(w, b):
    if dp[w][b] != -1:
        return dp[w][b]
    s = set()
    if w > 0:
        s.add(groudy(w-1, b+w))
    if b > 1:
        for i in range((b+1)//2, b):
            s.add(groudy(w, i))
    t = 0
    while t in s:
        t += 1
    dp[w][b] = t
    return t


g = 0
for w, b in zip(W, B):
    g ^= groudy(w, b)
print("First" if g > 0 else "Second")
