# https://leetcode.com/problems/binary-tree-inorder-traversal/

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# n = amount of nodes in tree
# Time: O(n) | Space: O(n)
def inorderTraversal(root):
    result = []

    def dfs(root):
        left, right = root.left, root.right
        if left:
            dfs(left)
        result.extend([root.val])
        if right:
            dfs(right)

    if root:
        dfs(root)

    return result

# Time: O(n) | Space: O(n)
def inorderTraversal(root):
    result = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result

tree = TreeNode(5,TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4))), TreeNode(6))

print(inorderTraversal(tree))