N = int(input())
num_list = [3, 5, 7]
ans = 0
for i in range(3, 10):
    num = pow(3, i)
    for j in range(num):
        check = [0, 0, 0]
        x = 0
        for k in range(i):
            d = j % 3
            x = 10*x+num_list[d]
            check[d] += 1
            j //= 3
        if (0 not in check) and x <= N:
            ans += 1

print(ans)
