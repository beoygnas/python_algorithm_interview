import sys
input = sys.stdin.readline 

N = int(input())
foods = []

for _ in range(N):
    x = input().split()
    k, food = int(x[0]), x[1:]
    foods.append(food)

foods.sort()

current  = [''] * 16

for food in foods :    
    reset = 0
    for i,f in enumerate(food) :
        if not reset and current[i] == f :
            continue
        else : 
            reset = 1
            offset = '' 
            for _ in range(i):
                offset += '--' 
            current[i] = f
            print(offset+f)
