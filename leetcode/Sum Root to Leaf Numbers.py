# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Time: O(n) | Space: O(1)
def sumNumbers(root):
    if not root: return 0
    sum = 0
    def dfs(node, curr):
        nonlocal sum
        children = [child for child in (node.left, node.right) if child is not None]
        for child in children:
            dfs(child, curr * 10 + child.val)
        if not children:
            sum += curr
    dfs(root, root.val)
    return sum
