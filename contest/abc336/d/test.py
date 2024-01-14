import random
N=random.randint(5, 10**2)
A=[ random.randint(1, 10**2) for _ in range(N) ]
print(N)
print(*A)