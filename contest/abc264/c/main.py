import itertools
H1,W1= map(int, input().split())
A=[list(map(int, input().split())) for _ in range(H1)]
H2,W2= map(int, input().split())
B=[list(map(int, input().split())) for _ in range(H2)]
for H in itertools.combinations(range(H1),H2):
    for W in itertools.combinations(range(W1),W2):
        newA=[[A[i][j] for j in W] for i in H]
        # print(newA)
        if newA==B:
            exit(print("Yes"))

print("No")