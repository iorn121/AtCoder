D=input()
directions = ['S', 'W', 'N', 'E']
ans=[]
for dd in D:
    for i,d in enumerate(directions):
        if dd == d:
            ans.append(directions[(i+2)%4])
            break
print(''.join(ans))