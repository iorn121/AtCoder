from re import T


A, B, C, D = map(int, input().split())

# check = [True]*201
# check[1] = False
# for i in range(2, 15):
#     for j in range(1, 201):
#         if j % i == 0:
#             if j//i != 1:
#                 check[j] = False

# sosuu = [x for x in range(1, 201) if check[x]]
# print(sosuu)

sosuu = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
N = len(sosuu)
Takahashi_win = False
for x in range(A, B+1):
    Aoki_win = False
    for y in range(C, D+1):
        if x+y in sosuu:
            Aoki_win = True
    # print(x)
    # print("Aoki_win" if Aoki_win else "Aoki_lose")
    if not Aoki_win:
        Takahashi_win = True
print('Takahashi' if Takahashi_win else 'Aoki')
