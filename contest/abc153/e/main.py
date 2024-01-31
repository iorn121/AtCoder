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

H,N=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(N)]
AB.sort(key=lambda x:-x[0]/x[1])
min_cost=[float('inf')]*(H+1)
min_cost[0]=0
for a,b in AB:
    for i in range(H):
        if i+a>H:
            min_cost[H]=min(min_cost[H],min_cost[i]+b)
        else:
            min_cost[i+a]=min(min_cost[i+a],min_cost[i]+b)
print(min_cost[H])