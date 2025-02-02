# 에라토스테네스 체처럼, 각각의 숫자를 배수를 곱해가면서 한다.
# 시간복잡도가 꽤 커보이긴하는데

N = int(input())
nums = [int(x) for x in input().split()]
sorted_nums = sorted(nums)
answer = {x:0 for x in sorted_nums}

M = sorted_nums[-1]

for num in sorted_nums :
    n_num = 2*num
    while n_num <= M :
        if n_num in answer : 
            answer[n_num] -= 1
            answer[num] += 1
        n_num += num

nums = [answer[x] for x in nums]
print(*nums)