# https://leetcode.com/problems/merge-two-binary-trees


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 0. 재귀 + dfs
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 두 트리를 어떻게 동시에 순회할까

        def dfs(node1, node2): 
            if node1 and node2 : 
                node = TreeNode(node1.val + node2.val)
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)
                return node
            else : 
                return node1 or node2
                
        return dfs(root1, root2)

# 1. 더 깔끔하게
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 두 트리를 어떻게 동시에 순회할까
        
        if root1 and root2 : 
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else : 
            return root1 or root2
                