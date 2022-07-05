# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Time: O(n) | Space: O(1)
def maxDepth(root, depth=0):
    if not root:
        return depth
    maxleft = maxDepth(root.left, depth+1)
    maxright = maxDepth(root.right, depth+1)
    return max(maxleft, maxright)