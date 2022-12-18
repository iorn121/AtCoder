N= int(input())

flg=True
first=set(["H","D","C","S"])
second=set(["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"])
all_s=set([])

for _ in range(N):
    S= input()
    if not (S[0] in first and S[1] in second and S not in all_s):
        flg= False
    all_s.add(S)



print("Yes" if flg else "No")
