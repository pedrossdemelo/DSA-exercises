# https://leetcode.com/problems/path-sum/

# Time: O(n) | Space: O(h)
def hasPathSum(root, targetSum):
    if not root:
        return False

    def toFindPathSum(node, curr):
        nonlocal targetSum
        children = [child for child in (node.left, node.right) if child is not None]
        for child in children:
            toFindPathSum(child, curr+child.val)
        if not children and curr == targetSum:
            raise Exception('Result found')

    try:
        toFindPathSum(root, root.val)
    except Exception:
        return True
    return False