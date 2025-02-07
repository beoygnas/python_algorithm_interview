import sys
input = sys.stdin.readline

N, M = [int(x) for x in input().split()]
arr = [int(input()) for _ in range(N)]

segment_tree = [[float('inf'), -float('inf')]] * (4*N)

def init_segment_tree(idx, start, end):
    if start==end :
        segment_tree[idx] = [arr[start], arr[start]]
    else : 
        mid = (start+end)//2
        init_segment_tree(2*idx, start, mid)
        init_segment_tree(2*idx+1, mid+1, end)
        segment_tree[idx] = [min(segment_tree[2*idx][0], segment_tree[2*idx+1][0]), max(segment_tree[2*idx][1], segment_tree[2*idx+1][1])]
    
def get_answer_from_segment_tree(idx, start, end, l, r): 
    
    if start==l and end==r : 
        return segment_tree[idx]
    
    mid = (l+r)//2
    if start > mid : 
        return get_answer_from_segment_tree(2*idx+1, start, end, mid+1, r)
    elif end <= mid :
        return get_answer_from_segment_tree(2*idx, start, end, l, mid)
    else : 
        l = get_answer_from_segment_tree(2*idx, start, mid, l, mid)
        r = get_answer_from_segment_tree(2*idx+1, mid+1, end, mid+1, r)
        return [min(l[0], r[0]), max(l[1], r[1])]
        
init_segment_tree(1, 0, N-1)
for _ in range(M):
    start, end = [int(x) for x in input().split()]
    print(*get_answer_from_segment_tree(1, start-1, end-1, 0, N-1))
