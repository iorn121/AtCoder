N= int(input())
from collections import defaultdict
dic=defaultdict(int)
used=set()
for _ in range(N):
    S=input()
    if S in used:
        print(f"{S}({dic[S]})")
    else:
        used.add(S)
        print(S)
    dic[S]+=1