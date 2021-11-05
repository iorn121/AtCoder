S = input()

S_list = []

for i in range(len(S)):
    newS = S[i:]+S[:i]
    S_list.append(newS)

S_list.sort()


print(S_list[0])
print(S_list[len(S_list)-1])
