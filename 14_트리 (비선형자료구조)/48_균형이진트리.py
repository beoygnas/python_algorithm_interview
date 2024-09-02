# https://leetcode.com/problems/balanced-binary-tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) : 
            if node is None : 
                return 0

            l, r = dfs(node.left), dfs(node.right)
            if abs(l-r) > 1  or l == -1 or r == -1: 
                return -1

            return max(l, r) + 1

        return dfs(root) != -1