N= int(input())
from collections import defaultdict
f_memo=defaultdict(int)
f_memo[0]=1
def f(x):
    if not f_memo[x]:
        x2=x//2
        x3=x//3
        f_memo[x]=f(x2)+f(x3)
    return f_memo[x]

print(f(N))