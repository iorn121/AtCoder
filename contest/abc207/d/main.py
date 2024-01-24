n = int(input())
s = [tuple(map(lambda x: int(x) * n, input().split())) for i in range(n)]
t = [tuple(map(lambda x: int(x) * n, input().split())) for i in range(n)]

sgx = sum(x for x, y in s) // n
sgy = sum(y for x, y in s) // n
tgx = sum(x for x, y in t) // n
tgy = sum(y for x, y in t) // n

s1 = [(x - sgx, y - sgy) for x, y in s]
t1 = [(x - tgx, y - tgy) for x, y in t]
s1.sort(key=lambda t: -(t[0]**2 + t[1]**2))
a, b = s1[0]
r2 = a ** 2 + b ** 2
t2 = {(c * r2, d * r2) for c, d in t1}
for c, d in t1:
    if c ** 2 + d ** 2 != r2:
        continue
    # (a, b) -(rot)-> r2 * (c, d)
    costh = a * c + b * d
    sinth = a * d - b * c
    t2_cand = {(a * costh - b * sinth, a * sinth + b * costh) for a, b in s1}
    if t2_cand == t2:
        print("Yes")
        exit()
print("No")
exit()









