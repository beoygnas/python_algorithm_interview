# https://leetcode.com/problems/course-schedule/
from typing import * 
import itertools
import collections


# 0. 재귀구조로 짠, 그래프 순환 체크 확인 + 가지치기
# 방향성은 거의 비슷. 구현이 오래걸림
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프가 순환구조인지 check
        # 코스마다 dfs 한번씩 해보면 될듯.
        
        # 그래프 생성
        graph = collections.defaultdict(list)
        for a,b in prerequisites : 
            graph[a].append(b)

        checked = [0] * numCourses
        # 재귀구조로 dfs
        def dfs(x, visited):
            if visited[x] : 
                return False
            if checked[x] : 
                return True 

            visited[x] = 1
            for nxt in graph[x] : 
                if not dfs(nxt, visited) : return False
            visited[x] = 0
            checked[x] = 1

            return True
        
        for p in prerequisites : 
            if not dfs(p[0], [0] * numCourses)  : 
                return False

        return True


# 1. 풀이는 일치하나, arrray 말고 set연산으로 대체
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for a,b in prerequisites : 
            graph[a].append(b)

        visited, checked = set(), set()
        
        def dfs(x):
            if x in visited : 
                return False
            if x in checked : 
                return True 

            visited.add(x)
            for nxt in graph[x] : 
                if not dfs(nxt) : 
                    return False
            
            visited.remove(x)
            checked.add(x)

            return True
        
        for p in prerequisites : 
            if not dfs(p[0])  : 
                return False

        return True
