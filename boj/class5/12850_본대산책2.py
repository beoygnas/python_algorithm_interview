## 폐급 코드
import collections

graph = collections.defaultdict(int)
d = collections.defaultdict(int)

graph[0] = [1, 2]
graph[1] = [0,2,3]
graph[2] = [0,1,3,4]
graph[3] = [1,2,4,5]
graph[4] = [2,3,5,6]
graph[5] = [3,4,7]
graph[6] = [4,7]
graph[7] = [5,6]

D = int(input())
def conquer(start, end, length): 
    if length == 2 : 
        if end in graph[start] :
            d[(start,end,length)] = 1
            return 1
        else : 
            d[(start,end,length)] = 0
            return 0
    
    counts = 0
    for k in range(8) : 
        l = d[(start, k, length//2+1)] if d[(start, k, length//2+1)] else conquer(start, k, length//2+1)
        r = d[(k, end, length-length//2)] if d[(k, end, length-length//2)] else conquer(k, end, length-length//2)
        counts +=  (l*r) 
        counts %= 1000000007
    
    d[(start,end,length)] = counts
    return counts

print(conquer(0, 0, D+1))