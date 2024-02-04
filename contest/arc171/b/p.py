import heapq
import collections
import itertools
MOD=998244353

def main(N,A):
    vacants = []
    ope=collections.defaultdict(list)
    for i in range(N):
        if A[i]==i+1:
            vacants.append(i+1)
        elif A[i]>i+1:
            ope[A[i]].append(i+1)
        else:
            return 0
    candidate=set([i for i in range(1,N+1)])
    print(ope)
    for k,v in ope.items():
        if k in candidate:
            candidate.remove(k)
        else:
            return 0
        for i in v[1:]:
            if i in candidate:
                candidate.remove(i)
            else:
                return 0
    print(vacants)
    print(candidate)
    cand=list(candidate)
    heapq.heapify(cand)
    cnt=0
    ans=1
    # print(cand)
    for v in vacants:
        while cand:
            x=heapq.heappop(cand)
            if x<=v:
                cnt+=1
            else:
                heapq.heappush(cand,x)
                break
            # print(x,cand)
        ans*=cnt
        print(ans,cnt,cand)
        ans%=MOD
        cnt-=1
    # print(ans)
    return ans


def another(N,A):
    ans=0
    for i in itertools.permutations(range(1,N+1)):
        B=[j for j in range(1,N+1)]
        P=list(i)
        for j in range(N):
            while B[j]<P[B[j]-1]:
                B[j]=P[B[j]-1]
        if B==A:
            ans+=1
    # print(ans)
    return ans