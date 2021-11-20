N, K = map(int, input().split())

score = []

for i in range(N):
    P = list(map(int, input().split()))
    score.append((sum(P), i))
    # print(sum(P),)

Ascore = score[:]
Ascore.sort(reverse=True)
num, j = Ascore[K-1]

# print(num, j)
for i in range(N):
    judge = score[i][0]
    # print(judge)
    print("Yes" if num <= 300+judge else "No")
