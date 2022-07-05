# https://leetcode.com/problems/recover-binary-search-tree/

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
def recoverTree(root):
    inorder, stack = [], []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        inorder.append((curr.val, curr))
        curr = curr.right
    n = len(inorder)
    left, right = 0, n-1
    maxleft, minright = inorder[left][0], inorder[right][0]
    start, end = right, left
    while left < n:
        nleft, nright = inorder[left][0], inorder[right][0]
        if nleft < maxleft:
            end = left
        else:
            maxleft = nleft
        if nright > minright:
            start = right
        else:
            minright = nright
        left += 1
        right -= 1
    inorder[start][1].val, inorder[end][1].val = inorder[end][0], inorder[start][0]

# Time: O(n) | Space: O(h)
def recoverTree(root):
    stack = []
    curr = root
    prev = TreeNode(float('-inf'))
    swapstart = swapend = None
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        # In a inorder traversal of a BST, all values
        # are sorted. Therefore the prev value must be
        # equal or smaller
        if prev.val > curr.val:
            if not swapstart:
                swapstart = prev
            swapend = curr
        prev = curr
        curr = curr.right
    swapstart.val, swapend.val = swapend.val, swapstart.val

root = TreeNode.from_list([3,1,4,None,None,2])
print(root)
recoverTree(root)
print(root)