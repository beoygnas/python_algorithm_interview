import sys
input = sys.stdin.readline

answer = 0
MOD = 1000000007
# 분할정복을 이용한 pow 개선
def pow_dc(a, b):
    if b==0:
        return 1
    if b==1 :
        return a
    
    half = pow(a, b//2)
    return half*half%MOD if b%2==0 else half*half*a%MOD

N = int(input())
arr = sorted(list(map(int, input().split())))
for i in range(N):
    j = N-1-i
    answer += arr[i] * ((pow_dc(2,i)-1)-(pow_dc(2,j)-1)) # 공집합인 경우를 빼야하므로

print(answer%MOD)    