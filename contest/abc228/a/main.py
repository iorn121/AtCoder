S, T, X = map(int, input().split())

if S > T:
    T += 24
if S > X:
    X += 24

print("Yes" if S <= X < T else "No")
