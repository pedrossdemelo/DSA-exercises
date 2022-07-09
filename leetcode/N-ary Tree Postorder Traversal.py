# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Time: O(n) | Space: O(height)
def postorder(root):
    postorder = []
    if not root:
        return postorder
    def dfs(node):
        for child in node.children:
            dfs(child)
        postorder.append(node.val)
    dfs(root)
    return postorder