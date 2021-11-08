N = int(input())

s = set()

for i in range(N):
    col = "".join(input())
    s.add(col)

print(len(s))
