
convert = input().split()
N = int(input())
A = []
for i in range(N):
    a = input()
    convert_a = 0
    for j in range(len(a)):
        convert_a += convert.index(a[j])*(10**(len(a)-j-1))
    A.append((convert_a, a))

A.sort()

for i in range(N):
    print(A[i][1])
