import sys
sys.setrecursionlimit(10**7)
arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
    
def dfs(start, end): 
    if start==end :
        print(arr[start])
    elif start > end :
        return
    else :
        value = arr[start]
        i = start+1
        while i < len(arr) and arr[i] <= value :
            i+=1
        dfs(start+1, i-1)
        dfs(i, end)
        print(arr[start])

dfs(0, len(arr)-1)