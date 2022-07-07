# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Time: O(n) | Space: O(h)
def maxDepth(root):
    maxDepth = 0
    if not root: return maxDepth
    def dfs(root=root, depth=1):
        nonlocal maxDepth
        if not root.children:
            maxDepth = max(maxDepth, depth)
        for child in root.children:
            dfs(child, depth+1)
    dfs()
    return maxDepth