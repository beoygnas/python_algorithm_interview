# https://leetcode.com/problems/invert-binary-tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 0. 재귀 + dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) :
            if node is None : 
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        return root
            
# 1. 반복 + dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs를 하면서 왼쪽 오른쪽 바꿔가면 될듯.

        stack = [root]

        while stack : 
            top = stack.pop()
            if top is None : 
                continue
            top.left, top.right = top.right, top.left
            stack.append(top.left)
            stack.append(top.right)

        return root
    
# 2. 반복 + bfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs를 하면서 왼쪽 오른쪽 바꿔가면 될듯.

        queue = collections.deque([root])

        while queue : 
            top = queue.pop()
            if top is None : 
                continue
            top.left, top.right = top.right, top.left
            queue.append(top.left)
            queue.append(top.right)

        return root
            

# 3. 파이썬 다운 방식
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root :
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root