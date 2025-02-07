N, B = [int(x) for x in input().split()]

matrix = [[0]*N for _ in range(N)]
for i in range(N):
    matrix[i] = [int(x)%1000 for x in input().split()]

def mat_mul(m1,m2): 
    # n번 A^2
    squred_matrix = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N): 
                squred_matrix[i][j] += m1[i][k] * m2[k][j]
                squred_matrix[i][j] %= 1000
    
    return squred_matrix

def answer(m, num): 
    if num == 1 :
        return m
    if num % 2 == 0 : 
        return answer(mat_mul(m,m), num//2)
    else :
        return mat_mul(answer(mat_mul(m,m), num//2), m)
    
ans_matrix = answer(matrix, B)
for m in ans_matrix:
    print(*m)