N = int(input())
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

X.sort()
Y.sort()
med = (N-1)//2
med_x, med_y = X[med], Y[med]
ans = 0
for i in range(N):
    ans += abs(X[i]-med_x)+abs(Y[i]-med_y)
# print(med_x, med_y)
print(ans)
