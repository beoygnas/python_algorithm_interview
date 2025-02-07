# backtracking + Factorial

import collections
import copy

N = int(input())
answer = 0

factorial = [1] * 14
for i in range(1, 14): 
    factorial[i] = factorial[i-1] * i
vis = collections.defaultdict(int)

def combination(n, r): 
    return factorial[n] // (factorial[r] * factorial[n-r])

def fun(li):
    global answer, vis
    if len(li) == 4 :
        if sum(li) == N :
            tmp_li = copy.copy(li)
            rest_num = 13
            value = 1
            while any(tmp_li):
                print(tmp_li)
                min_num = 0
                tmp_li.sort()
                for n in tmp_li :
                    if n > 0 :
                        min_num = n
                        break
                value *= combination(rest_num, min_num)
                rest_num = 13 - min_num
                for i in range(len(tmp_li)) :
                    if tmp_li[i] : 
                        tmp_li[i] -= min_num
    else :
        for i in range(1, 14): 
            li.append(i)
            fun(li)
            li.pop()
    return

fun([])
print(answer)