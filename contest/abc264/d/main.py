S= list(input())
goal="atcoder"
from collections import deque
d=dict()
q=deque()
q.appendleft(S)
d["".join(S)]=0
while q:
    s=q.popleft()
    for i in range(6):
        ns=s[:]
        ns[i],ns[i+1]=ns[i+1],ns[i]
        # print(s,ns)
        if "".join(ns) in d:
            continue
        d["".join(ns)]=d["".join(s)]+1
        q.append(ns)
    if goal in d:
        exit(print(d[goal]))

