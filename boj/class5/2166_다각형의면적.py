# 1. 다각형에 대해서 좌표 값을 줌
# 풀이 핵심은, 좌표의 외적을 통해 삼각형의 넓이를 구하기
# CCW 알고리즘 : counter clockwise (https://kangminjun.tistory.com/106)
# 음수일 수도 있다!
N = int(input())
coords = []
for _ in range(N) :
    x, y = [int(x) for x in input().split()]
    coords.append((x, y))

def getAreaCCW(a, b, c) :
    return ((a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0]))/2

answer = 0
for i in range(1, N-1) :
    answer += getAreaCCW(coords[0], coords[i], coords[i+1])

print(abs(round(answer, 1)))