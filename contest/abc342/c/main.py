N=int(input())
S=input()
Q=int(input())
convert="abcdefghijklmnopqrstuvwxyz"
for _ in range(Q):
  c,d=input().split()
  convert=convert.replace(c,d)
ans=[]
for s in S:
  new_s=convert[ord(s)-97]
  ans.append(new_s)
print("".join(ans))