import collections
N=int(input())
color={}
for _ in range(N):
    A,C=map(int,input().split())
    if C not in color:
        color[C]=A
    else:
        color[C]=min(color[C],A)
# print(color.values())
print(max(color.values()))