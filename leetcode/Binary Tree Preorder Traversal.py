# https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) | Space: O(n)
def preorderTraversal(root):
    preorder = []
    def dfs(node):
        if not node: return
        preorder.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return preorder

# Time: O(n) | Space: O(n)
def preorderTraversal(root):
    preorder, stack, curr = [], [], root
    while curr or stack:
        if not curr:
            curr = stack.pop()
        preorder.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        curr = curr.left
    return preorder

tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))

print(preorderTraversal(tree))
