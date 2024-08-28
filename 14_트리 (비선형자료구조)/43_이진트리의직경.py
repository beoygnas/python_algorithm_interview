# https://leetcode.com/problems/diameter-of-binary-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. 왼쪽 dfs, 오른쪽 dfs 하고 각각 level 더하면 될듯
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node) : 
            nonlocal answer

            if node is None :
                return 0
            
            l_depth = dfs(node.left)
            r_depth = dfs(node.right)
            
            answer = max(answer, l_depth + r_depth)    

            return max(l_depth, r_depth) + 1

        dfs(root)
        return answer
        