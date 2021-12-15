N = int(input())
A_list = []
B_list = []
ans = 10**6
for i in range(N):
    A, B = map(int, input().split())
    A_list.append((A, i))
    B_list.append((B, i))
    ans = min(ans, A+B)
A_list.sort()
B_list.sort()
a = 0
b = 0
while A_list[a][1] == B_list[b][1]:
    if A_list[a+1][0] > B_list[b+1][0]:
        b += 1
    else:
        a += 1
# print(A_list)
# print(B_list)
# print(a, b)
ans = min(ans, max(A_list[a][0], B_list[b][0]))
print(ans)
