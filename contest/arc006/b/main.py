N, L = map(int, input().split())
S = [input() for _ in range(L)]
circle = input()
goal = circle.index('o')
for i in range(L-1, -1, -1):
    if S[i][goal-(goal != 0)] == '-':
        goal -= 2
    elif S[i][goal+(goal != N*2-2)] == '-':
        goal += 2

print(goal//2+1)
