# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) | Space: O(n)
def rightSideView(root):
    rights = []
    queue = deque([(root, 0)])
    while queue:
        curr, depth = queue.pop()
        if len(rights) == depth:
            rights.append(curr.val)
        else:
            rights[depth] = curr.val 
        if curr.left:
            queue.appendleft((curr.left, depth+1))
        if curr.right:
            queue.appendleft((curr.right, depth+1))
    return rights