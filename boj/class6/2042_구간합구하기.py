import math
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = [int(x) for x in input().split()]
arr = [0]
for _ in range(N) :
    arr.append(int(input()))

segment_tree = [0] * (4*N+1)

def make_st(start, end, idx) : 
    global arr, segment_tree
    if start==end: 
        segment_tree[idx] = arr[start]
    else : 
        mid = (start + end) // 2
        segment_tree[idx] = make_st(start, mid, 2*idx) \
            + make_st(mid+1, end, 2*idx+1)
        
    return segment_tree[idx]
            
def sum_st(start, end, l, r, idx): 
    if l > end or r < start :
        return 0
    if l <= start and r >= end :
        return segment_tree[idx]    
    mid = (start+end)//2
    return sum_st(start, mid, l, r, 2*idx) + sum_st(mid+1, end, l, r, 2*idx+1)
        
def update_st(start, end, arr_idx, num, s_idx): 
    if arr_idx < start or arr_idx > end :
        return
    segment_tree[s_idx] += num
    if start == end :
        return
    else :
        mid = (start+end) // 2
        update_st(start, mid, arr_idx, num, 2*s_idx)
        update_st(mid+1, end, arr_idx, num, 2*s_idx+1)
    
    return segment_tree[s_idx]
        

make_st(1, N, 1)

for _ in range(M+K):
    a, b, c = [int(x) for x in input().split()]
    
    if a == 1 :
        update_st(1, N, b, c-arr[b], 1)
        arr[b] = c
    else : 
        print(sum_st(1, N, b, c, 1))