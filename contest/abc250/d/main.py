import bisect
import math


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


def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


N = int(input())
ans = 0
primes = sieve_of_eratosthenes(int(pow(N, 1/3))+10)
cnt = 0
for i in primes:
    if i**3 > N:
        break
    j = bisect.bisect_right(primes, N//(i**3))
    ans += min(cnt, j)
    cnt += 1
    # print(i, j, ans)
print(ans)
