import collections
import sys
input = sys.stdin.readline

R, C, M = [int(x) for x in input().split()]
sharks = []
answer = 0
for _ in range(M) :
    sharks.append([int(x) for x in input().split()])
    
for idx in range(1, C+1):
    if len(sharks) == 0 :
        break
    
    sharks.sort(key=lambda x : (-abs(idx-x[1]),-x[0]))
    if sharks[-1][1] == idx : 
        answer += sharks[-1][4]
        sharks.pop()
    
    new_shark = collections.defaultdict(list)
    
    for i in range(len(sharks)): 
        r,c,s,d,z = sharks[i]
        size, cur = [R, r] if d <= 2 else [C, c]
        left_distance = s % ((size-1)*2)
            
        while left_distance : 
            if d in [1,4] :
                side_size = cur-1
                cur = max(cur-side_size, cur-left_distance)
            else :
                side_size = size-cur
                cur = min(cur+side_size, cur+left_distance) 
            
            left_distance -= min(side_size, left_distance)
            if left_distance :
                if d == 1 : 
                    d=2
                elif d == 2 : 
                    d=1
                elif d == 3: 
                    d=4
                elif d == 4:
                    d=3
        
        shark = [cur,c,s,d,z] if d<=2 else [r,cur,s,d,z]
        x, y = shark[0], shark[1]
        if not new_shark[(x, y)] or new_shark[(x,y)][4] < shark[4] :
            new_shark[(x,y)] = shark
            
    sharks = list(new_shark.values())

print(answer)