# https://leetcode.com/problems/range-sum-of-bst

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. 클래스 변수로 처리하고 재귀
class Solution:
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
    
        def dfs(node) :        
            if node :
                dfs(node.right)
                self.value += node.val
                node.val = self.value
                dfs(node.left)
        
            return node    
            
        dfs(root)
        return root
