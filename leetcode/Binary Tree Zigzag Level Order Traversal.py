# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self == None:
            return ""
        if self.left == self.right == None:
            return str(self.val)
        ans = str(self.val)
        if self.left != None:
            ans = ans + "(" + str(self.left) + ")"
        else:
            ans = ans + "()"
        if self.right != None:
            ans = ans + "(" + str(self.right) + ")"
        return ans

from collections import deque

def tree(arr, i=0):
    root = None
    if i < len(arr) and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = tree(arr, 2 * i + 1)
        root.right = tree(arr, 2 * i + 2)

    return root

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

root = tree([3,9,20,None,None,15,7])

print(zigzagLevelOrder(root))