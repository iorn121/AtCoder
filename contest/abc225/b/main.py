n = int(input())
counter = [0] * (n + 1)

for i in range(n-1):
    a, b = map(int, input().split())
    counter[a] += 1
    counter[b] += 1

print("Yes" if n - 1 in counter else "No")
