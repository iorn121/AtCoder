H, W = map(int, input().split())
A = [input() for _ in range(H)]

cnt = sum(A[i].count('#') for i in range(H))

print('Possible' if cnt == H+W-1 else 'Impossible')
