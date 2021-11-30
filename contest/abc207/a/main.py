A, B, C = map(int, input().split())

sum_list = [A+B, B+C, C+A]

print(max(sum_list))
