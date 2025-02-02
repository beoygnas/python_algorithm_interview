# DP
import sys
input=sys.stdin.readline

n = int(input())
graph = []


s1 = [int(x) for x in input().split()]
s2 = s1.copy()

for _ in range(n-1):
    new = [int(x) for x in input().split()]
    s1[0], s1[1], s1[2] = new[0]+max(s1[0], s1[1]), new[1]+max(s1[0], s1[1], s1[2]), new[2]+max(s1[1], s1[2])
    s2[0], s2[1], s2[2] = new[0]+min(s2[0], s2[1]), new[1]+min(s2[0], s2[1], s2[2]), new[2]+min(s2[1], s2[2])
        
print(max(s1), min(s2))

