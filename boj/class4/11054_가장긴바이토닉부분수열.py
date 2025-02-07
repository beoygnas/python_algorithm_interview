N = int(input())
arr = [int(x) for x in input().split()]


def get_longest_array(li) :
    d = [(0, -1)]
    for i in range(len(li)): 
        idx = i
        max_cnt, max_val = -1, -1
        
        while idx > -1:
            if li[i] >= d[idx][1] and d[idx][0] > max_cnt : 
                max_cnt, max_val = d[idx][0], d[idx][1]
            idx -= 1
            
        d.append((max_cnt + (0 if max_val==li[i] else 1), li[i]))
    return d
    
d1, d2 = get_longest_array(arr), get_longest_array(arr[::-1])

print(max([x[0]+y[0] for x,y in zip(d1[1:], d2[1:][::-1])])-1)
