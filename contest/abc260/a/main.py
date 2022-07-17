S= input()

from collections import defaultdict
d=defaultdict(int)

for s in S:
    d[s] +=1

for k,v in d.items():
    if v==1:
        exit(print(k))
print(-1)