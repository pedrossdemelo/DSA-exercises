# https://leetcode.com/problems/sum-of-left-leaves/

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


# Time: O(n) | Space: O(height of tree)
def sumOfLeftLeaves(root):
    sum = 0
    stack = [(root, False)]
    while stack:
        node, isLeft = stack.pop()
        if (node.left, node.right) == (None, None) and isLeft: # If it is a left leaf node
            sum += node.val
        if node.left:
            stack.append((node.left, True))
        if node.right:
            stack.append((node.right, False))
    return sum


root = TreeNode.from_list([3,9,20,None,None,15,17])
print(sumOfLeftLeaves(root))