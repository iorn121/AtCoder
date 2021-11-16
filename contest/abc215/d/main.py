import math
N, M = map(int, input().split())

A = list(map(int, input().split()))

s = set()

# 素因数分解　numの素因数をdict形式で返す


def prime_factriz(num):
    fact = {}
    for i in range(2, num):
        if i*i > num:
            break
        while num % i == 0:
            if i not in fact:
                fact[i] = 0
            fact[i] += 1
            num //= i
        if num < i:
            break
    if num != 1:
        fact[num] = 1
    return fact


for i in A:
    for j in prime_factriz(i).keys():
        s.add(j)

ans = [True]*(M+1)
ans[0] = False
for i in s:
    for j in range(i, M+1, i):
        if ans[j]:
            ans[j] = False

print(sum(ans))
for i in range(M+1):
    if ans[i]:
        print(i)
