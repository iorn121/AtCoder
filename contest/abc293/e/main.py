def matmul(A, B, mod):
    N = len(A)
    K = len(A[0])
    M = len(B[0])

    c = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N) :
        for j in range(K) :
            for k in range(M) :
                c[i][k] += A[i][j] * B[j][k] 
                c[i][k] %= mod
    return c

def pow_matrix(A, p, mod):
    n = len(A)
    c = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while p > 0 :
        if p%2 == 1 :
            c = matmul(c, A, mod)
        A = matmul(A, A, mod)
        p //= 2
    return c

def main():
    A,X,M=map(int, input().split())
    A_matrix=[[A,1],[0,1]]
    X_matrix=[[0],[1]]
    ans_matric=pow_matrix(A_matrix,X,M)
    ans=matmul(ans_matric,X_matrix,M)[0][0]
    print(ans)


if __name__ == "__main__":
    main()