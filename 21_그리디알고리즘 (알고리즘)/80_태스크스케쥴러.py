# https://leetcode.com/problems/task-scheduler
import heapq

# 0. 우선순위 큐
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        answer = 0 
        answer_list = []
        counter, counter_interval, in_heap = collections.Counter(tasks), defaultdict(int), defaultdict(bool)
        
        heap = []
        most_common_task = counter.most_common(1)[0][0]
        heapq.heappush(heap, (-counter[most_common_task], most_common_task))
        remained_tasks = len(tasks)
        
        while remained_tasks : 
            answer += 1
            
            if heap : 
                _, task = heapq.heappop(heap)
                counter[task] -= 1
                remained_tasks -= 1
                in_heap[task] = False
                answer_list.append(task)
                counter_interval[task] = n+1
            else :
                answer_list.append('idle')
                            
            for k in counter :
                if counter_interval[k] > 0 : 
                   counter_interval[k] -= 1
                if counter_interval[k] == 0 and counter[k] > 0 and in_heap[k] is False:
                    heapq.heappush(heap, (-counter[k], k))
                    in_heap[k] = True
                    
        return answer