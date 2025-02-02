# 정렬 + 투포인터
# 4000 * 4000 = 16,000,000 짜리 2개 만들기를 * 3 (2개로 분할하는 경우의수) = 48,000,000

N = int(input())
ABCD = [[], [], [], []]

for _ in range(N) : 
    for i, x in enumerate([int(x) for x in input().split()]):
        ABCD[i].append(x)

answer = 0
ab, cd = [], []
for i in range(N) :
    for j in range(N) :
        ab.append(ABCD[0][i] + ABCD[1][j])
        cd.append(ABCD[2][i] + ABCD[3][j])
        
ab.sort()
cd.sort()
    
i, j = 0, N**2-1
while i < N**2 and j >= 0 :
    total_sum = ab[i] + cd[j]
    if total_sum == 0 :
        nxt_i, nxt_j = i, j
        while nxt_i < N**2 and ab[nxt_i] == ab[i]:
            nxt_i += 1
        while nxt_j >= 0 and cd[nxt_j] == cd[j]:
            nxt_j -= 1
        answer += (nxt_i - i) * (j - nxt_j)
        i, j = nxt_i, nxt_j
    elif total_sum > 0 :
        j-=1
    else :
        i+=1
             
print(answer)