N = int(input())
ans = 0

for i in range(1, 16):
    num = int('1'*i)
    if N < num:
        break
    else:
        ans += 1
        num_max = num
        num_min = num
        while num_min*10 <= N:
            num_min *= 10
            num_max = (num_max+1)*10-1
            ans += min(num_max, N)-num_min+1

print(ans)
