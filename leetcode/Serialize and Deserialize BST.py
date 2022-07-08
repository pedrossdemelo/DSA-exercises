# https://leetcode.com/problems/serialize-and-deserialize-bst/

from collections import deque
import json
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr):
        n = len(arr)
        root = cls(arr[0])
        queue = deque([root])
        i = 1
        while queue and i < n:
            curr = queue.popleft()
            if i < n and arr[i] != None:
                left = cls(arr[i])
                curr.left = left
                queue.append(left)
            i += 1
            if i < n and arr[i] != None:
                right = cls(arr[i])
                curr.right = right
                queue.append(right)
            i += 1
        return root

    def __repr__(s):
        if s == None:
            return ""
        if s.left == s.right == None:
            return str(s.val)
        ans = str(s.val)
        if s.left != None:
            ans = ans + "(" + str(s.left) + ")"
        else:
            ans = ans + "()"
        if s.right != None:
            ans = ans + "(" + str(s.right) + ")"
        return ans


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return '[]'
        queue = deque([root])
        levelorder = []
        while queue:
            node = queue.popleft()
            levelorder.append(node.val if node else None)
            if not node: continue
            queue.append(node.left)
            queue.append(node.right)
        return json.dumps(levelorder)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = json.loads(data)
        if not data:
            return
        root = TreeNode(data[0])
        i, n = 1, len(data)
        queue = deque([root])
        while queue and i < n:
            node = queue.popleft()
            if i < n and data[i] != None:
                left = TreeNode(data[i])
                node.left = left
                queue.append(left)
            i += 1
            if i < n and data[i] != None:
                right = TreeNode(data[i])
                node.right = right
                queue.append(right)
            i += 1
        return root

c = Codec()

root = TreeNode.from_list([1,None,2,None,3,None,4,None,5])
seria = c.serialize(root)
print(seria)
deseria = c.deserialize(seria)
print(deseria)