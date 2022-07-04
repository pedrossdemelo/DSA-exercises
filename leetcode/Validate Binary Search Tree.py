# https://leetcode.com/problems/validate-binary-search-tree/

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


# Time: O(n) | Space: O(n)
def isValidBST(root):
    stack, inorder = [], []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        curr = stack.pop()
        if inorder and inorder[-1] >= curr.val:
            return False
        inorder.append(curr.val)
        curr = curr.right
    return True


# Time: O(n) | Space: O(n)
def isValidBST(root):
    inorder, result = [], True

    def inorderdfs(node):
        nonlocal result
        if not node or result == False:
            return
        inorderdfs(node.left)
        if inorder and inorder[-1] >= node.val:
            result = False
            return
        inorder.append(node.val)
        inorderdfs(node.right)

    inorderdfs(root)
    return result


# Time: O(n) | Space: O(n)
def isValidBST(root, min=float("-inf"), max=float("inf")):
    if not root:
        return True
    if not min < root.val < max:
        return False
    return isValidBST(root.left, min, root.val) and isValidBST(
        root.right, root.val, max
    )


root = TreeNode.from_list([3, 1, 5, 0, 2, 4, 6])
print(isValidBST(root))
