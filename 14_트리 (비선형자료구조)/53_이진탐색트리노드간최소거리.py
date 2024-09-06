# https://leetcode.com/problems/minimum-distance-between-bst-nodes
import sys 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. 가지치기 하면서 dfs    
class Solution:
    prev = -sys.maxsize
    answer = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    # 왼쪽의 가장 큰 값과 
    # 오른쪽의 가장 작은 값을 비교하자.
        
        if root.left : 
            self.minDiffInBST(root.left)
        
        self.answer = min(self.answer, root.val - self.prev)
        self.prev = root.val

        if root.right : 
            self.minDiffInBST(root.right)

        return self.answer

# 1. 반복으로 풀기
class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:   
        
        stack = []
        node = root
        prev, result = -sys.maxsize, sys.maxsize
        
        while stack or node : 
            while node : 
                stack.append(node)
                node = node.left
            
            node = stack.pop()
        
            result = min(result, node.val-prev)
            prev = node.val
            node = node.right

        return result