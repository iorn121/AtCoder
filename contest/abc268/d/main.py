import itertools
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
Ts = set(T)


if N == 1:
    if len(S[0]) < 3 or S[0] in Ts:
        exit(print(-1))
    else:
        exit(print(S[0]))

rest = sum([len(S[i]) for i in range(N)])

max_num = 16-rest
bar_list = ["_"*i for i in range(1, max_num+1)]

bar_list_use = []

for bars in itertools.product(*[bar_list for _ in range(N-1)]):
    if sum([len(bar) for bar in bars]) <= max_num:
        bar_list_use.append(bars)

for bars in bar_list_use:
    for nS in itertools.permutations(S):
        word = []
        for i in range(N-1):
            word.append(nS[i])
            word.append(bars[i])
        word.append(nS[-1])
        ans = "".join(word)
        # print(ans)
        if ans not in Ts:
            exit(print(ans))
print(-1)
