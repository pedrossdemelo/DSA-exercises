# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

# Time: O(n) | Space: O(n)
def preorder(root):
    preorder = []
    if not root:
        return preorder
    def dfs(root):
        preorder.append(root.val)
        for child in root.children:
            dfs(child)
    dfs(root)
    return preorder

root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(1)])
print(preorder(root))