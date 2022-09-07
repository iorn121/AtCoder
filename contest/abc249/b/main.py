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


S = input()
if len(S) == len(set(list(S))) and not S.isupper() and not S.islower():
    print("Yes")
else:
    print("No")
