import itertools
S1=input()
S2=input()
S3=input()

chars = set(S1) | set(S2) | set(S3)
if len(chars) > 10:
    print("UNSOLVABLE")
    exit()

candidates=set(range(10))

for candidate in itertools.permutations(candidates, len(chars)):
    char_to_num = dict(zip(chars, candidate))
    if char_to_num[S1[0]] == 0 or char_to_num[S2[0]] == 0 or char_to_num[S3[0]] == 0:
        continue
    num1 = int("".join(str(char_to_num[c]) for c in S1))
    num2 = int("".join(str(char_to_num[c]) for c in S2))
    num3 = int("".join(str(char_to_num[c]) for c in S3))
    if num1 == 0 or num2 == 0 or num3 == 0:
        continue
    if num1 + num2 == num3:
        print(num1)
        print(num2)
        print(num3)
        exit()
print("UNSOLVABLE")