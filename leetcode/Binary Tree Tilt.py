# https://leetcode.com/problems/binary-tree-tilt/submissions/

# Time: O(n) | Space: O(1)
def findTilt(root):
    result = 0
    def dfs(node):
        nonlocal result
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        result += abs(left-right)
        return node.val + left + right
    dfs(root)
    return result