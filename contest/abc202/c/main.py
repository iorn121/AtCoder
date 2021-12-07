from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A_dict = defaultdict(int)
convert = defaultdict(int)
for i in range(N):
    A_dict[A[i]] += 1
    convert[B[C[i]-1]] += 1
ans = 0
for k, v in A_dict.items():
    ans += convert[k]*v

print(ans)
