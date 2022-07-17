N,M = map(int, input().split())
bits=[0]*N
for i in range(N):
    bit=0
    T=int(input())
    A=list(map(int, input().split()))
    for a in A:
        bit|=1<<(M-a)
    bits[i]=bit
S=list(map(int, input().split()))
bit_s=0
for i,s in enumerate(reversed(S)):
    if s:
        bit_s|=s<<i
# print(bits)
# print(bit_s)
base=[-1]*(M+1)

cnt=0

for bit in bits:
    while bit:
        l=bit.bit_length()
        if base[l]==-1:
            base[l]=bit
            break
        bit^=base[l]
    if bit==0:
        cnt+=1
# print(base,cnt)

while bit_s:
    l=bit_s.bit_length()
    if base[l]==-1:
        exit(print(0))
    bit_s^=base[l]
MOD= 998244353
print(pow(2,cnt,MOD))
