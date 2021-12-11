N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB = []
d = {}
for i in range(N):
    if A[i] not in d:
        d[A[i]] = []
    d[A[i]].append(B[i])
    AB.append((A[i], B[i]))
AB.sort()
B_use = []
ans = 0
for a in sorted(d):
    for b in d[a]:
        B_use.append(b)
    B_use.sort()
    for b in d[a]:
        left = -1
        right = len(B_use)
        while right-left > 1:
            mid = (left+right)//2
            if B_use[mid] < b:
                left = mid
            else:
                right = mid
        ans += i-left

print(ans)
