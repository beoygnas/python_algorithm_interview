# https://leetcode.com/problems/minimum-height-trees

from typing import *

# 0. 형태에 상관없이, 리프노드를 차곡차곡 지워나간다.
# 최악의 시간복잡도
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 또한 답은 무조건 1개 or 2개
        if n == 1 : 
            return [0]

        graph = collections.defaultdict(list)
        for a,b in edges : 
            graph[a].append(b)
            graph[b].append(a)

        while len(graph) > 2:
            leaves = [v for v in graph if len(graph[v]) == 1]
            for leaf in leaves : 
                graph[graph[leaf][0]].remove(leaf)
                del graph[leaf]

        return graph.keys()
        
        
# 1. 불필요한 n^2 계산은 딱 한번만
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 형태에 상관없이, 리프노드를 차곡차곡 지워나간다.
        # 또한 답은 무조건 1개 or 2개
        if n == 1 : 
            return [0]

        graph = collections.defaultdict(list)
        for a,b in edges : 
            graph[a].append(b)
            graph[b].append(a)

        leaves = [v for v in graph if len(graph[v]) == 1]
        
        while n > 2:    
            n -= len(leaves)
            
            new_leaves = []
            for leaf in leaves : 
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            
            leaves = new_leaves
        
        return leaves
    