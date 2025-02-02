# 다이나믹 프로그래밍
# 시간복잡도 : 100,000 * 2 * 10
# 총 발의 경우의 수는 10가지니까 가능
# 비용에 따라, 4가지로 가능

import itertools

ddr = [int(x) for x in input().split()]
feet = itertools.combinations([0,1,2,3,4], 2)
d = {foot:[float('inf')]*(len(ddr)-1) for foot in feet}
d[(0,ddr[0])][0] = 2

for i, nxt in enumerate(ddr[:-1]) :
    if i==0 : 
        continue
    
    for foot in d :
        if d[foot][i-1] == float('inf') :
            continue
        
        for j in range(2) : 
            if foot[j] == nxt : 
                d[foot][i] = min(d[foot][i-1]+1, d[foot][i])
            
            nxt_foot = list(foot)
            if foot[j] == 0 :
                nxt_foot[j], offset = nxt, 2
            elif abs(foot[j] - nxt) == 2 :
                nxt_foot[j], offset = nxt, 4
            else : 
                nxt_foot[j], offset = nxt, 3
                    
            nxt_foot = tuple(sorted(nxt_foot))
            if nxt_foot[0] != nxt_foot[1] :
                d[nxt_foot][i] = min(d[foot][i-1]+offset, d[nxt_foot][i])
    
print(min([d[x][-1] for x in d]))