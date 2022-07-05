# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Time: O(n) | Space: O(h)
def maxPathSum(root):
    maxpath = float("-inf")

    def dfs(node):
        nonlocal maxpath
        if not node:
            return 0
        # The best path in the left cannot be lower than 0.
        # If it is, the best path is not going there at all
        maxleft = max(dfs(node.left), 0)
        # Same goes for the right path
        maxright = max(dfs(node.right), 0)
        # We have the option to traverse both max paths in the
        # left and right, including our own value
        maxpath = max(maxpath, maxleft + node.val + maxright)
        # If we use both left and right paths AND a parent node,
        # then one or more nodes will be illegally visited twice.

        # Therefore, we must choose the max path from either left
        # or right so that our parent node can connect to the
        # current node and then traverse the max path below
        return node.val + max(maxleft, maxright)

    dfs(root)
    return maxpath
