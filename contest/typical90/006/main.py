import pprint
N, K = map(int, input().split())
S = input()


# def find_min(s, k):
#     if k > 1:
#         new_s = list(map(ord, s[:-k+1]))
#     else:
#         new_s = list(map(ord, s))
#     # print(new_s, len(new_s))
#     c = chr(min(new_s))
#     c_index = s.index(c)
#     # print(c, c_index)
#     return c, c_index


# ans = []
# start = 0
# partS = S[:]
# for i in range(K, 0, -1):
#     # print("---")
#     # print(f"partS: {partS} => i:{i},{partS[:-i+1]}")
#     s, offset = find_min(partS, i)
#     ans.append(s)
#     start += offset+1
#     partS = S[start:]
# print("".join(ans))

def calc_next(S):
    N = len(S)

    res = [[N]*26 for _ in range(N+1)]

    for i in range(N-1, -1, -1):
        res[i][:] = res[i+1][:]
        res[i][ord(S[i])-ord("a")] = i

    return res


res = calc_next(S)
# pprint.pprint(res)
ans = []
now = -1
for i in range(K):
    for j in range(26):
        p = res[now+1][j]
        if N-p >= K-i:
            ans.append(chr(ord("a")+j))
            now = p
            break
print("".join(ans))
