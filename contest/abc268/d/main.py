N,M = map(int, input().split())
S=[input() for _ in range(N)]
T=[input() for _ in range(M)]
Ts=set(T)

import itertools

rest=sum([len(S[i]) for i in range(N)])+N-1
for i in range(rest):
    nS=S[:]
    if i>0:
        for _ in range(i):
            nS.append("")
    for combo in itertools.permutations(nS):
        # print("_".join(combo))
        test_ans="_".join(combo)
        if test_ans[0]=="_":
            continue
        if test_ans not in Ts:
            exit(print(test_ans))

        if rest==0:
            continue




print(-1)