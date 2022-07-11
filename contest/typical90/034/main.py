from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
cnt = 0
ans = 0
left = 0
s = set()
for a in A:
    if a in s:
        cnt += 1
        d[a] += 1
    else:
        if len(s) <= K:
            cnt += 1
            d[a] += 1
            s.add(a)
        while len(s) > K:
            d[A[left]] -= 1
            cnt -= 1
            if d[A[left]] == 0:
                s.remove(A[left])
            left += 1
    # print(a, s, cnt)
    ans = max(ans, cnt)
print(ans)
