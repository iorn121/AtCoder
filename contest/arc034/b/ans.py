#!/usr/bin/env python3

N = int(input())
ans = []
for i in range(1, N+1):
    x = sum(list(map(int, str(i))))
    if x+i == N:
        ans.append(i)
print(len(ans))
if ans:
    print(*ans, sep="\n")
exit()
