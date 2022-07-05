# https://leetcode.com/problems/symmetric-tree/

# Time: O(n) | Space: O(n)
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr):
        n = len(arr)
        root = cls(arr[0])
        queue = deque([root])
        i = 1
        while queue and i < n:
            curr = queue.popleft()
            if i < n and arr[i] != None:
                left = cls(arr[i])
                curr.left = left
                queue.append(left)
            i += 1
            if i < n and arr[i] != None:
                right = cls(arr[i])
                curr.right = right
                queue.append(right)
            i += 1
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


def isSymmetric(root):
    if not root:
        return True
    levelorder = []
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if len(levelorder) == depth:
            levelorder.append([node.val if node else None])
        else:
            levelorder[depth].append(node.val if node else None)
        if not node:
            continue
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))
    for level in levelorder:
        n = len(level)
        if n > 1 and n % 2:
            return False
        if not level[: n // 2] == level[: n // 2 - 1 : -1]:
            return False
    return True


# Time: O(n) | Space: O(1)
def isSymmetric(root):
    if not root:
        return True

    def simmetric(root1, root2):
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False
        return simmetric(root1.left, root2.right) and simmetric(root1.right, root2.left)

    return simmetric(root.left, root.right)

# Time: O(n) | Space: O(1)
def isSymmetric(root):
    if not root:
        return True
    left, right = root.left, root.right

    def inverse(root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        inverse(root.left)
        inverse(root.right)
        return root

    def equal(blue, red):
        if blue is None or red is None:
            return blue == red
        if blue.val != red.val:
            return False
        return equal(blue.left, red.left) and equal(blue.right, red.right)

    return equal(left, inverse(right))

root = TreeNode.from_list([1, 2, 2, None, 3, None, 3])
print(isSymmetric(root))
