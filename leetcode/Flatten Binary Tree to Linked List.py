# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) | Space: O(n)
def flatten(root):
    nums = []
    def dfs(node):
        if not node:
            return
        nums.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    curr = root
    for num in nums[1:]:
        curr.left = None
        curr.right = TreeNode(num)
        curr = curr.right

# Time: O(n) | Space: O(1)
def flatten(root):
    if not root:
        return
    right = root.right
    root.right = root.left
    root.left = None
    flatten(root.right)
    flatten(right)
    while root.right:
        root = root.right
    root.right = right

tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, right=TreeNode(6)))

print(flatten(tree))