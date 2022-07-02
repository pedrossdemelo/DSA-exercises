# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr, i=0):
        root = None
        if i < len(arr) and arr[i] is not None:
            root = cls(arr[i])
            root.left = cls.from_list(arr, 2 * i + 1)
            root.right = cls.from_list(arr, 2 * i + 2)

        return root

    def __repr__(s):
        if s == None:
            return ""
        if s.left == s.right == None:
            return str(s.val)
        ans = str(s.val)
        if s.left != None:
            ans = ans + "(" + str(s.left) + ")"
        else:
            ans = ans + "()"
        if s.right != None:
            ans = ans + "(" + str(s.right) + ")"
        return ans

from collections import deque

# Time: O(n) | Space: O(n)
def zigzagLevelOrder(root):
    result = []
    if not root: return result
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.pop()
        if len(result) == depth:
            result.append(deque([node.val]))
        elif depth % 2:
            result[depth].appendleft(node.val)
        else:
            result[depth].append(node.val)
        children = (node.left, node.right)
        for child in children:
            if child:
                queue.appendleft((child, depth + 1))
    return result

root = TreeNode.from_list([3,9,20,None,None,15,7])
print(zigzagLevelOrder(root))