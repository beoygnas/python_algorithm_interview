N, M = map(int, input().split())
arr = list(map(int, input().split()))
st = [0 for _ in range(4040404)]

def init(start, end, idx): 
    if start == end :
        st[idx] = arr[start]
    else :
        mid = (start+end)//2
        st[idx] = max(init(start, mid, 2*idx), init(mid+1, end, 2*idx+1))
    return st[idx]

def get(start, end, l, r, idx):
    if r < start or l > end:
        return 0
    if l <= start and r >= end :
        return st[idx]
    mid = (start+end)//2
    return max(get(start, mid, l, r, 2*idx), get(mid+1, end, l, r, 2*idx+1))
    
init(0,N-1,1)
for i in range(M, N-M+2): 
    print(get(1, N, i-M+1, i+M-1, 1), end=' ')