N, K = map(int, input().split())

A = list(map(int, input().split()))
A_sort = sorted(A)

X = K//N
K %= N
get_line = A_sort[K]

for a in A:
    print(X+1 if a < get_line else X)
