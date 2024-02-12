from sortedcontainers import SortedList
from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB=[[a,b] for a,b in zip(A,B)]
AB.sort(key=lambda x: (x[0],-x[1]))
dq = deque(AB)
# print(dq)
ans = 0
S = SortedList([])
while dq:
    A,B = dq[0]
    cnt = 0
    while dq and dq[0] == [A,B]:
        dq.popleft()
        S.add(B)
        cnt += 1
    ans += cnt * (len(S) - S.bisect_left(B))

print(ans)