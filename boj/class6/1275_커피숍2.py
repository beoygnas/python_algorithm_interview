import sys
input = sys.stdin.readline

N, Q = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
st = [0] * (4*N)

def init(start, end, idx): 
    if start == end : 
        st[idx] = arr[start]
    else : 
        mid = (start + end) // 2
        st[idx] = init(start, mid, 2*idx) + init(mid+1, end, 2*idx+1)
    return st[idx]

def st_sum(start, end, l, r, idx):
    if r < start or l > end : 
        return 0
    if l <= start and r >= end : 
        return st[idx]
    mid = (start + end) // 2
    return st_sum(start, mid, l, r, 2*idx) + st_sum(mid+1, end, l, r, 2*idx+1)

def st_update(start, end, arr_idx, value, s_idx):
    if arr_idx < start or arr_idx > end :
        return
    st[s_idx] += value
    if start != end :
        mid = (start + end) // 2
        st_update(start, mid, arr_idx, value, 2*s_idx)
        st_update(mid+1, end, arr_idx, value, 2*s_idx+1)
        
init(0, N-1, 1)
for _ in range(Q):
    x,y,a,b = [int(x) for x in input().split()]
    x,y = min(x, y), max(x,y)
    print(st_sum(0,N-1,x-1,y-1,1))    
    st_update(0,N-1,a-1,b-arr[a-1],1)
    arr[a-1] = b