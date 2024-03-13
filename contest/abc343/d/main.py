import collections
N,T=map(int,input().split())
dic=collections.defaultdict(int)
dic[0]=N
num=[0]*N
for _ in range(T):
    A,B=map(int,input().split())
    cur=num[A-1]
    new=cur+B
    num[A-1]=new
    dic[cur]-=1
    dic[new]+=1
    if dic[cur]==0:
        del dic[cur]
    print(len(dic))
