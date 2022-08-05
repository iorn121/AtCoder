L,R=map(int, input().split())
MOD=10**9+7
def count_number(num: int)-> int:
    digit,count=1,0
    while True:
        left=10**(digit-1)-1
        right=min(num,10**digit-1)
        count+=((right+1)*right-(left+1)*left)//2*digit
        
        if num<=right:
            return count
        digit+=1

print((count_number(R)-count_number(L-1))%MOD)