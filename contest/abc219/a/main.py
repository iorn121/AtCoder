X = int(input())
if 90 <= X:
    print("expert")
elif 70 <= X < 90:
    print(90-X)
elif 40 <= X < 70:
    print(70-X)
else:
    print(40-X)
