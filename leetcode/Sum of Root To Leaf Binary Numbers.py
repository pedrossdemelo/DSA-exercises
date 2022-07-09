# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

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


# Time: O(n) | Space: O(h)
def sumRootToLeaf(root):
    stack = [(root, 0)]
    sum = 0
    while stack:
        curr, path = stack.pop()
        path = (path << 1) | curr.val # path = path * 2 + 1
        if (curr.left, curr.right) == (None, None):
            sum += path
        if curr.left:
            stack.append((curr.left, path))
        if curr.right:
            stack.append((curr.right, path))
    return sum

root = TreeNode.from_list([1,0,1,0,1,0,1])
print(sumRootToLeaf(root))