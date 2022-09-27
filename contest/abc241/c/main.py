N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(N-5):
        cnt = 0
        for k in range(6):
            ni = i
            nj = j+k
            if S[ni][nj] == "#":
                cnt += 1
        if cnt >= 4:
            exit(print("Yes"))
for i in range(N-5):
    for j in range(N):
        cnt = 0
        for k in range(6):
            ni = i+k
            nj = j
            if S[ni][nj] == "#":
                cnt += 1
        if cnt >= 4:
            exit(print("Yes"))
for i in range(N-5):
    for j in range(N-5):
        cnt = 0
        for k in range(6):
            ni = i+k
            nj = j+k
            if S[ni][nj] == "#":
                cnt += 1
        if cnt >= 4:
            exit(print("Yes"))
for i in range(5, N):
    for j in range(N-5):
        cnt = 0
        for k in range(6):
            ni = i-k
            nj = j+k
            if S[ni][nj] == "#":
                cnt += 1
        if cnt >= 4:
            exit(print("Yes"))
print("No")
