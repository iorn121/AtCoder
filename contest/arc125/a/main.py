N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

S_ = set(S)
T_ = set(T)
if not T_ <= S_:
    print(-1)
else:
    if T_ == {S[0]}:
        print(len(T))
    else:
        first = S[0]
        second = [1 if first == 0 else 0][0]
        forward_index = S.index(second)-1
        backward_index = S[::-1].index(second)
        ans = min(forward_index, backward_index)
        now = first
        for t in T:
            ans += 1+(now != t)
            now = t
        print(ans)
