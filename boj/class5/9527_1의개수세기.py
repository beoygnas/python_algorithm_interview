A, B = [int(x) for x in input().split()]

def S(x) :
    num, n = 1, 0
    while num <= x :
        num *= 2 
        n += 1
    
    num_one = 0
    for i in range(n): 
        s, r = x//(2**i), x%(2**i)
        num_one += s//2 * (2**i)    
        
        if s%2 == 1: 
            num_one += r
    return num_one

print(S(B+1) -S(A))
            
        
    
    
