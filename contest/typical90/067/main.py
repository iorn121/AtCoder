N, K = map(int, input().split())
N = str(N)


def convert9base5replace(S: str):
    base10 = int(S, 8)
    if base10 == 0:
        return "0"
    base9 = []
    while base10:
        remainder = base10 % 9
        if remainder == 8:
            remainder = 5
        base9.append(str(remainder))
        base10 //= 9
    return "".join(base9[::-1])


for _ in range(K):
    N = convert9base5replace(N)

print(N)
