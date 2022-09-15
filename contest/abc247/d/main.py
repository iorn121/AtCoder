from collections import deque


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


q = deque()

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    inst = query[0]
    if inst == 1:
        q.append((query[1], query[2]))
    elif inst == 2:
        c = query[1]
        ans = 0
        while c:
            x, y = q[0]
            if y <= c:
                c -= y
                ans += x*y
                q.popleft()
            else:
                ans += x*c
                q[0] = (x, y-c)
                c = 0
        print(ans)
