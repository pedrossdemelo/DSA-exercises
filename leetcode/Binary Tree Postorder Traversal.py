# https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return f"{self.val}"

# Time: O(n) | Space: O(n)
def postorderTraversal(root):
    postorder = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)
        postorder.append(node.val)
    dfs(root)
    return postorder


# Time: O(n) | Space: O(n)
def postorderTraversal(root):
    postorder, stack, curr = [], [], root
    while stack or curr:
        while curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        if curr.right and len(stack) > 0 and stack[-1] == curr.right:
            stack.pop()
            stack.append(curr)
            curr = curr.right
        else:
            postorder.append(curr.val)
            curr = None

    return postorder

tree = TreeNode(1, right=TreeNode(2, TreeNode(3)))
print(postorderTraversal(tree))