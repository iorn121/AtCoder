N, Q = map(int, input().split())
A = list(map(int, input().split()))

# if N == 1:
#     exit(print(0))

inconvenience = [A[i+1]-A[i] for i in range(N-1)]
total_inconvenience = sum([abs(i) for i in inconvenience])

for _ in range(Q):
    L, R, V = map(int, input().split())
    if L-2 >= 0:
        total_inconvenience -= abs(inconvenience[L-2])
        inconvenience[L-2] += V
        total_inconvenience += abs(inconvenience[L-2])
    if R < N:
        total_inconvenience -= abs(inconvenience[R-1])
        inconvenience[R-1] -= V
        total_inconvenience += abs(inconvenience[R-1])
    print(total_inconvenience)
