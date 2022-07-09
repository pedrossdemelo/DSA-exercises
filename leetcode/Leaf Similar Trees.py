# https://leetcode.com/problems/leaf-similar-trees/

# Time: O(n) | Space: O(height + leafs)
def leafSimilar(root1, root2):
    leaf1, leaf2 = [], []
    def dfs(node, leaf):
        if not node: return
        if not node.right and not node.left:
            leaf.append(node.val)
            return
        dfs(node.left, leaf)
        dfs(node.right, leaf)
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2