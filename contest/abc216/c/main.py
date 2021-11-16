N = int(input())

ans = ""

now = N

while N > 0:
    if N % 2 == 0:
        N //= 2
        ans += "B"
    else:
        N -= 1
        ans += "A"

print(ans[::-1])
