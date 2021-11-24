s_list = set()

for _ in range(4):
    S = input()
    s_list.add(S)

print("Yes" if len(s_list) == 4 else "No")
