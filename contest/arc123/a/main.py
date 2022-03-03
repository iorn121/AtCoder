A, B, C = map(int, input().split())

if A+C <= B*2:
    print(B*2-A-C)
else:
    print((A+C+1)//2-B+(A+C) % 2)
