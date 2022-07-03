# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque
import json


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
    def serialize(self, root):
        data = []
        queue = deque([root])
        last = 0
        while queue:
            curr = queue.popleft()
            if not curr:
                data.append('null')
            else:
                data.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
                last = len(data)
        del data[last:]
        return '[' + ','.join(data) + ']'

    def deserialize(self, data):
        if data == "[]":
            return None
        data = json.loads(data)
        n = len(data)
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1
        while queue and i < n:
            curr = queue.popleft()
            if i < n and data[i] != None:
                left = TreeNode(data[i])
                curr.left = left
                queue.append(left)
            i += 1
            if i < n and data[i] != None:
                right = TreeNode(data[i])
                curr.right = right
                queue.append(right)
            i += 1
        return root

c = Codec()
root = TreeNode.from_list([1,2,3,None,None,4,5])
print(root)
seria = c.serialize(root)
print(seria)
deseria = c.deserialize(seria)
print(deseria)
