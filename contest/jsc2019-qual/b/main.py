N, K = map(int, input().split())
A = list(map(int, input().split()))
N = len(A)
MOD = 10**9+7
ans = 0
all_right_num = []

for i, a in enumerate(A):
    all_num = 0
    right_num = 0
    for j, b in enumerate(A):
        if a > b:
            all_num += 1
            if i < j:
                right_num += 1
    all_right_num.append((all_num, right_num))

for i in range(N):
    all_num, right_num = all_right_num[i]
    ans += (K-1)*K//2*all_num
    ans %= MOD
    ans += K*right_num
    ans %= MOD

print(ans)
