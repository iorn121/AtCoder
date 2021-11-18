N = int(input())
A = list(map(int, input().split()))
ans = [(A[i], i+1) for i in range(N)]
ans.sort(reverse=True)
print(ans[1][1])
