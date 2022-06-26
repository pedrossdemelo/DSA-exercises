# https://leetcode.com/problems/binary-tree-order-traversal/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree(arr, i=0):
    root = None
    if i < len(arr):
        if arr[i] is not None:
            root = TreeNode(arr[i])
            root.left = tree(arr, 2 * i + 1)
            root.right = tree(arr, 2 * i + 2)

    return root

# Time: O(n) | Space: O(n)
def levelOrder(root):
    q = deque()
    if root:
        q.append((root, 0))
    res = []
    while q:
        curr, depth = q.popleft()
        if len(res) == depth:
            res.append([])
        res[depth].append(curr.val)
        if curr.left:
            q.append((curr.left, depth+1))
        if curr.right:
            q.append((curr.right, depth+1))
    return res

root = tree([3,9,20,None,None,15,7])

print(levelOrder(root))