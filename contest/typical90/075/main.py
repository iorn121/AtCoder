N= int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factor_list = factorization(N)
if len(factor_list)==1 and factor_list[0][1]==1:
    print(0)
else:
    sum_factor=sum([fl[1] for fl in factor_list])
    # print(factor_list)
    # print(sum_factor)
    for i in range(1,50):
        if 2**i>=sum_factor:
            exit(print(i))