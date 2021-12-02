A, B, C = map(int, input().split())


if A == B:
    print("=")
    exit()
elif C % 2 == 0:
    if A == B*-1:
        print("=")
        exit()
    print("<" if abs(A) < abs(B) else ">")
    exit()
else:
    print("<" if A < B else ">")
