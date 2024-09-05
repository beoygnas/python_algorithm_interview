# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 0. 
# 가운데 하나 찝고
# 재귀로 왼쪽 트리 구성, 오른쪽 트리 구성
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:    
    

        def make_bst(nums) : 
            
            if len(nums) >= 3 : 
                mid = len(nums)//2 
                node = TreeNode(nums[mid]) 
                node.left = make_bst(nums[:mid])
                node.right = make_bst(nums[mid+1:])
                return node
            
            elif len(nums) == 2 :
                node = TreeNode(nums[0])
                node.right = TreeNode(nums[1])  
                return node
        
            elif len(nums) == 1 :
                return TreeNode(nums[0])
            
            else :
                return None

        return make_bst(nums)
    

# 1. 좀 더 세련되게 코드 작성
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:    
    # 가운데 하나 찝고
    # 재귀로 왼쪽 트리 구성, 오른쪽 트리 구성
        if not nums:
            return None
        
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node