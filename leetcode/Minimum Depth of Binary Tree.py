# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Time: O(n) | Space: O(n)
def minDepth(root):
    if not root: return 0
    queue = deque([(root, 1)])
    while queue:
        curr, depth = queue.pop()
        l, r = curr.left, curr.right
        if not l and not r:
            return depth
        if l:
            queue.appendleft((l, depth+1))
        if r:
            queue.appendleft((r, depth+1))