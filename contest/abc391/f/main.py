import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

hq = [(-(A[0]*B[0] + B[0]*C[0] + C[0]*A[0]), 0, 0, 0)]
seen = set([(0, 0, 0)])

for t in range(K):
    v, i, j, k = heapq.heappop(hq)
    if t == K - 1:
        print(-v)
    if j + 1 < N and (i, j + 1, k) not in seen:
        heapq.heappush(hq, (-(A[i]*B[j + 1] + B[j + 1]*C[k] + C[k]*A[i]), i, j + 1, k))
        seen.add((i, j + 1, k))
    if k + 1 < N and (i, j, k + 1) not in seen:
        heapq.heappush(hq, (-(A[i]*B[j] + B[j]*C[k + 1] + C[k + 1]*A[i]), i, j, k + 1))
        seen.add((i, j, k + 1))
    if i + 1 < N and (i + 1, j, k) not in seen:
        heapq.heappush(hq, (-(A[i + 1]*B[j] + B[j]*C[k] + C[k]*A[i + 1]), i + 1, j, k))
        seen.add((i + 1, j, k))
