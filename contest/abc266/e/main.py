N= int(input())
E=3.5
ans=[i+1 for i in range(6)]
for i in range(N-1):
    
    for me in range(1,7):
        if E>me:
            ans[me-1]=E
    E=sum(ans)/6
    # print(ans)
print(E)