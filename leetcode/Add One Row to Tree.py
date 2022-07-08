# https://leetcode.com/problems/add-one-row-to-tree/submissions/

from collections import deque


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


# Time: O(n) | Space: (depth)
def addOneRow(root, val, depth):
    if depth == 1:
        return TreeNode(val, left=root)
    def dfs(node, cdepth=1):
        nonlocal depth
        if not node:
            return
        if cdepth == depth - 1:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
            return
        dfs(node.left, cdepth+1)
        dfs(node.right, cdepth+1)
    dfs(root)
    return root

root = TreeNode.from_list([4,4,4,4,4,4,4,4,4])
print(addOneRow(root, 9, 3))