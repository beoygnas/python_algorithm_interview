N = int(input())

# d[i][j][k] : i자리수인 수이며 j로 끝나는 모든 계단수의 개수, k는 사용된 bit 수

d = [[[0] * (1024) for _ in range(10)] for _ in range(N+1)]

# initialize 
for n in range(1,10) :
    d[1][n][1<<n] = 1
    
for i in range(1, N) :
    for j in range(10) : 
        for k in range(1024) : 
            if j < 9 :
                d[i+1][j+1][k|(2**(j+1))] += d[i][j][k]
                d[i+1][j+1][k|(2**(j+1))] %= 1000000000
            if j > 0 :
                d[i+1][j-1][k|(2**(j-1))] += d[i][j][k]
                d[i+1][j-1][k|(2**(j-1))] %= 1000000000
                

answer = 0
for i in range(10) :
    answer += d[N][i][1023]
    answer %= 1000000000

print(answer)

