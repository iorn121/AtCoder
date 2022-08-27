A=tuple(map(int, input().split()))
B=tuple(map(int, input().split()))
C=tuple(map(int, input().split()))
D=tuple(map(int, input().split()))

def gaiseki(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return 1 if tc1*tc2<0 and td1*td2<0 else 0

isCross=0
isCross+=gaiseki(A,B,C,D)
isCross+=gaiseki(A,C,B,D)
isCross+=gaiseki(A,D,B,C)
# print(isCross)
print("No" if isCross==0 else "Yes")