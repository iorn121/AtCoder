
def main():
    INF=pow(2,61)-1.0
    N,D=map(int,input().split())
    W=list(map(int,input().split()))
    ave=sum(W)/D
    heavy=[0.0]*(1<<N)
    for i in range(1<<N):
        for j in range(N):
            if (i>>j)&1:
                heavy[i]+=W[j]
    # print(heavy)
    bit=[{i} for i in range(1<<N)]
    for j in range(N):
        bi=1<<j
        for i in range(1<<N):
            if i&bi:
                for k in bit[i^bi]:
                    bit[i].add(k);
    for i in range(1<<N):
        bit[i]=(i.bit_count(),i,bit[i])
    bit.sort(key=lambda x:x[0])
    # print(bit)
    dp=[[INF]*(D+1) for i in range(1<<N)]
    dp[0][0]=0.0
    for b,i,aft in bit:
        if i==0:
            continue
        for j in range(1,min(b+1,D+1)):
            ans=INF
            for k in aft:
                ans=min(ans,(ave-heavy[k])**2+dp[i^k][j-1])
            dp[i][j]=ans
    print(dp[-1][-1]/D)


if __name__ == "__main__":
    main()
