# 정렬 + 가장긴부분수열
import bisect
import sys
import collections
input = sys.stdin.readline

N = int(input())
arr = sorted([[int(x) for x in input().split()] for _ in range(N)])

lis, index = [], []
for x,y in arr :
    idx = bisect.bisect_left(lis, y)
    if idx == len(lis) : 
        lis.append(y)
    else:
        lis[idx] = y
    index.append(idx)
        
cnt = len(lis)-1
q = collections.deque()
print(lis)
print(index)
print(arr)
for i in range(len(index)-1, -1, -1):
    print(i, cnt, index[i], arr[i])
    if index[i] == cnt:
        cnt -= 1
    else:
        # LIS에 포함되지 않는 경우를 저장.
        q.appendleft(arr[i])

print(len(arr) - len(lis))
for k in q:
    print(k[0])