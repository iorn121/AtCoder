S=input()
SS=[]
st=0
for i,s in enumerate(S):
    if s=="(" or s==")":
        en=i
        if st+1!=en:
            SS.append([st,en])
        st=i
        if s==")" and SS[-1]=="(":
            SS.pop()
        else:
            SS.append(s)
print(SS)
q=[]
ans=[]

def change(s):
    if s.isupper():
        return s.lower()
    else:
        return s.upper()

for s in SS:
    if s==")":
        while q[-1]!="(" and q:
            bs,bt=q.pop()
            print(bs,bt)
            q.append([bt,bs])
        q.pop()
    else:
        q.append(s)
    # print(q)
    
print("".join(q))