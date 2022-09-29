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


def f(s: str):
    convert = {"p": "d", "d": "p"}
    for i in range(len(s)):
        s[i] = convert[s[i]]
    return s[::-1]


N = int(input())
S = list(input())
# print(f(S))
l = -1

for i, s in enumerate(S):
    if l == -1 and s == "p":
        l = i
    if l != -1 and s == "d":
        break
ans = "".join(S)
for r in range(l, N):
    ans = min(ans, "".join(S[:l]+f(S[l:r+1])+S[r+1:]))

# print(S[:l], f(S[l:r+1]), S[r+1:])
print("".join(ans))
