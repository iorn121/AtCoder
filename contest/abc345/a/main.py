S=input()
if S[0]!="<" or S[-1]!=">":
    exit(print("No"))
for s in S[1:-1]:
    if s!="=":
        exit(print("No"))
print("Yes")