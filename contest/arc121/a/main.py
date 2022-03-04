N = int(input())
x = [0]*N
y = [0]*N
for i in range(N):
    x[i], y[i] = map(int, input().split())

x_max = max(x)
x_min = min(x)
y_max = max(y)
y_min = min(y)

l = [0]*N
for i in range(N):
    l[i] = max([abs(x_max-x[i]), abs(x_min-x[i]),
               abs(y_min-y[i]), abs(y_max-y[i])])
l.sort()
print(l[-3])
