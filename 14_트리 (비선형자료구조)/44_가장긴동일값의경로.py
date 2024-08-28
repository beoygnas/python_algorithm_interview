# https://leetcode.com/problems/longest-univalue-path


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 0.   dfs, 밑의 노드를 검산      
class Solution:
    answer = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # 밑에 dfs 돌리고, 값이 맞으면 갱신
        
        def dfs(node) :
            if node is None : 
                return 0
        
            left = dfs(node.left)
            right = dfs(node.right)

            if not (node.left and node.left.val == node.val) : 
                left = 0
            if not (node.right and node.right.val == node.val) : 
                right = 0
            
            self.answer = max(self.answer, left + right)
            return max(left, right) + 1
            
            
            
        dfs(root)
        
        return self.answer 