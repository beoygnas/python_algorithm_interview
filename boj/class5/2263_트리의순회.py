import sys
sys.setrecursionlimit(1000000)

n = int(input())

in_order = [int(x) for x in input().split()]
post_order = [int(x) for x in input().split()]
pre_order = []

in_order_idx = {x:i for i,x in enumerate(in_order)}
post_order_idx = {x:i for i,x in enumerate(post_order)}

def func(in_start, in_end, post_start, post_end):
    if in_start <= in_end and post_start <= post_end : 
        num = post_order[post_end]    
        pivot = in_order_idx[num]
        pre_order.append(num)
        left_counts = pivot - in_start
        func(in_start, pivot-1, post_start, post_start+left_counts-1)
        func(pivot+1, in_end, post_start+left_counts, post_end-1)

func(0,n-1, 0, n-1)
print(*pre_order)