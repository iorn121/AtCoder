S=input()
ans_set=set()
for i in range(len(S)):
    for j in range(i,len(S)):
        ans_set.add(S[i:j+1])
print(len(ans_set))