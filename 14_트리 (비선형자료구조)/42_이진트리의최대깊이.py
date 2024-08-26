# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. dfs + 재귀
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # 재귀 dfs
        def dfs(node, depth) :
            if node is None : 
                return depth
            else : 
                return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        
        return dfs(root, 0)
    
# 1. 반복 + bfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # 재귀 dfs
        def dfs(node, depth) :
            if node is None : 
                return depth
            else : 
                return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
        
        
        def bfs(node) : 
            q = collections.deque()
            q.append((node, 0))

            answer = 0    
            while q : 
                cur, depth = q.popleft()
                if cur is None : 
                    answer = max(answer, depth)
                else : 
                    q.append((cur.left, depth + 1))
                    q.append((cur.right, depth + 1))

            return answer
        return bfs(root)

                

