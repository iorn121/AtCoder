N = int(input())

if N % 2 == 1:
    print("")
else:
    K = N//2

    def dfs(l, r, s):
        if l == 0 and r == 0:
            print(s)
            return
        if l > 0:
            dfs(l-1, r, s+"(")
        if l < r:
            dfs(l, r-1, s+")")
    dfs(K, K, "")
