# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


import sys 
from typing import * 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 0. 전위, 중위 순회의 관계를 이용한 분할 정복.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder : 
            node = TreeNode(preorder.pop(0))
            idx = inorder.index(node.val)
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node
        