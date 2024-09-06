# https://leetcode.com/problems/range-sum-of-bst
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. 가지치기 하면서 dfs    
class Solution:
    answer = 0
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # 가지치기 하면서 dfs
        if root :
            if root.val >= low and root.val <= high : 
                self.answer += root.val
            
            if root.val >= low : 
                self.rangeSumBST(root.left, low, high) 
            if root.val <= high : 
                self.rangeSumBST(root.right, low, high) 
    
        return self.answer


        