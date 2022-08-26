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


H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
visited = [[False]*W for _ in range(H)]
dxy = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

x, y = 0, 0
visited[0][0] = True
while True:
    dy, dx = dxy[G[y][x]]
    x += dx
    y += dy
    if not (0 <= x < W and 0 <= y < H):
        x = x-dx+1
        y = y-dy+1
        break
    if visited[y][x]:
        exit(print(-1))
    visited[y][x] = True
print(y, x)
