N = int(input())

if N == 1:
    exit(print("Not Prime"))
if N == 2 or N == 3 or N == 5:
    exit(print("Prime"))
if N % 2 == 0:
    exit(print("Not Prime"))
if sum(map(int, list(str(N)))) % 3 == 0:
    exit(print("Not Prime"))
if N % 10 == 5:
    exit(print("Not Prime"))
print("Prime")
