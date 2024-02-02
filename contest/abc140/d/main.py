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

N,K=map(int,input().split())
S=input()
import itertools
groups=[len(list(itr)) for n, itr in itertools.groupby(S)]
# print(groups)
# print(sum(x-1 for x in groups))
ans=sum(x-1 for x in groups)+min(2*K,len(groups)-1)
print(ans)