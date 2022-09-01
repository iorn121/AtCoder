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


def factorical(A, B):
    if B == 0:
        return A
    return factorical(B, A % B)


N, A, B = map(int, input().split())
if A < B:
    A, B = B, A
total = N*(N+1)//2
An = N//A
Bn = N//B
AB = A*B//factorical(A, B)
ABn = N//AB

A_total = A*An*(An+1)//2
B_total = B*Bn*(Bn+1)//2
AB_total = AB*ABn*(ABn+1)//2

# print(factorical(A, B))
# print(A_total, B_total, AB_total)
print(total-A_total-B_total+AB_total)
