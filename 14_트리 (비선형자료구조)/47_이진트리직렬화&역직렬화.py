# https://leetcode.com/problems/serialize-and-deserialize-binary-tree)
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    # 완전 이진트리로 encode, decode 할 때 쉽도록
    def serialize(self, root):
        data = ""
        q = collections.deque([(root, 0)])
        
        while q : 
            cur, idx = q.popleft()
            
            if cur is None : 
                continue
            data += f"{idx}:{cur.val},"
            q.append((cur.left, idx*2+1))
            q.append((cur.right, idx*2+2))

        return data

    def deserialize(self, data):
        tree_list = collections.defaultdict(lambda: None)
        data = data.split(',')[:-1]
        
        for x in data :
            idx, value = x.split(':')
            tree_list[int(idx)] = int(value)

        if tree_list[0] is None : 
            return None
        
        root = TreeNode(tree_list[0])
        q = collections.deque([(root, 0)])
        
        while q : 
            cur, idx = q.popleft()
        
            if cur is None: 
                continue

            cur.left = TreeNode(tree_list[idx*2+1]) if tree_list[idx*2+1] is not None else None
            cur.right = TreeNode(tree_list[idx*2+2]) if tree_list[idx*2+2] is not None else None
            q.append((cur.left, idx*2+1))
            q.append((cur.right, idx*2+2))

        return root

        
# 1. 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # 완전 이진트리로 encode, decode 할 때 쉽도록
    def serialize(self, root):
        # bfs로 왼쪽 -> 오른쪽 하도록 탐색
        

        queue =collections.deque([root])
        result = ['#']
        
        while queue : 
            node = queue.popleft()
            if node :
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else : 
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data):
        
        print(data)
        if data == "# #" : 
            return None
        
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        q = collections.deque([root])
        idx = 2

        while q :
            node = q.popleft()
            if nodes[idx] is not '#' :
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1

            if nodes[idx] is not '#' :
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        
        return root 