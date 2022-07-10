S = input()
T = input()


ns = len(S)
nt = len(T)
if ns > nt:
    exit(print("No"))

s_list = []
t_list = []

s = S[0]
cnt = 0
for i, x in enumerate(S):
    if x == s:
        cnt += 1
    else:
        s_list.append((s, cnt))
        cnt = 1
        s = x
s_list.append((s, cnt))

t = T[0]
cnt = 0
for i, x in enumerate(T):
    if x == t:
        cnt += 1
    else:
        t_list.append((t, cnt))
        cnt = 1
        t = x
t_list.append((t, cnt))

# print(s_list)
# print(t_list)
if len(t_list) != len(s_list):
    exit(print("No"))
flg = True
for i, (x, num) in enumerate(s_list):
    if x != t_list[i][0]:
        flg = False
    if num != t_list[i][1]:
        if num < 2 or num > t_list[i][1]:
            flg = False

print("Yes" if flg else "No")
