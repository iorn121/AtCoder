N = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))
time = min(T)
index = T.index(time)
ans = [time]

for i in range(N-1):
    newIndex = (i+index) % N
    time = min(time+S[newIndex], T[(newIndex+1) % N])
    ans.append(time)

for i in range(N):
    newIndex = (i-index) % N
    print(ans[newIndex])
