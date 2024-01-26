N=int(input())
A=list(map(int,input().split()))

num_bits=[0]*60
for a in A:
    for i in range(60):
        if (1<<i)&a:
            num_bits[i]+=1

ans=0
MOD=10**9+7
multiplierMOD=[2**i%MOD for i in range(60)]
for i,num in enumerate(num_bits):
    num_pair=num*(N-num)%MOD
    ans+=multiplierMOD[i]*num_pair%MOD
    ans%=MOD
    # print(i,num,ans)
print(ans)