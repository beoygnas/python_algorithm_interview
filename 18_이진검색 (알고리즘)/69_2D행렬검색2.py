# https://leetcode.com/problems/search-a-2d-matrix-ii

import bisect
from typing import * 

# 0. binary search 통한 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(max(m log n, n log m))
        for row in matrix : 
            i = bisect.bisect_left(row, target)
            if i < len(row) and row[i] == target :
                return True
        
        return False
    
# 1. 투포인터라고 하기엔 애매하지만 그런 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(n + m)
        i, j = 0, len(matrix[0]) - 1
        
        while i < len(matrix) and j >= 0 : 
            if matrix[i][j] > target : 
                j -= 1
            elif matrix[i][j] < target : 
                i += 1
            else : 
                return True
        
        return False
            