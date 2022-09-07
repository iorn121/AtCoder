from random import *


def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# ランダムな整数を割り当て
table = {}
for a in A:
    table[a] = randrange(1 << 60)
for b in B:
    table[b] = randrange(1 << 60)

# print(table)

hashA = [0]
setA = set()
for a in A:
    if a in setA:
        hashA.append(hashA[-1])
    else:
        setA.add(a)
        hashA.append(hashA[-1] ^ table[a])

# print(hashA)

hashB = [0]
setB = set()
for b in B:
    if b in setB:
        hashB.append(hashB[-1])
    else:
        setB.add(b)
        hashB.append(hashB[-1] ^ table[b])

# print(hashB)

Q = int(input())
for _ in range(Q):
    X, Y = map(int, input().split())
    print("Yes" if hashA[X] == hashB[Y] else "No")
