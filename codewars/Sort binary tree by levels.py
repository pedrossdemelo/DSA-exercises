# https://www.codewars.com/kata/sort-binary-tree-by-levels/train/python
from collections import defaultdict


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    nodes_at_depth = defaultdict(list)

    def dfs(node, depth=0):
        nodes_at_depth[depth].append(node.value)
        if node.left:
            dfs(node.left, depth + 1)
        if node.right:
            dfs(node.right, depth + 1)

    dfs(node)

    return [value for values in nodes_at_depth.values() for value in values]


print(
    tree_by_levels(
        Node(
            Node(None, Node(None, None, 4), 2),
            Node(Node(None, None, 5), Node(None, None, 6), 3),
            1,
        )
    )
)
