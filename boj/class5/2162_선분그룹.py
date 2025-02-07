import collections
# Union-find
# 모든 그룹과 만나는지 안만나는지 체크 (직선의 방정식)

N = int(input())

# 세점이 시계방향인지, 반시계방향인지 체크
def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1

# 만나면 True
def check(x1,y1,x2,y2,x3,y3,x4,y4): 
    
    l1 = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
    l2 = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)
    
    if l1 <= 0 and l2 <= 0:
        if l1 == 0 and l2 == 0:
            d1 = max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2)
            d2 = max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2)
            if d1 and d2:
                return True
            return False
        else:
            return True
    return False

root = [] 
arr = []

def find(x):
    if root[x] != x :
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x, y = find(x), find(y)
    if x<y: root[y]=x
    else: root[x]=y
    
    
    
for i in range(N):
    root.append(i)
    arr.append([int(x) for x in input().split()])
    for j in range(i):
        if check(*arr[i], *arr[j]):
            union(i,j)
            
root=[find(x) for x in root]  
counter = collections.Counter(root)
print(len(counter))
print(counter.most_common(1)[0][1])
