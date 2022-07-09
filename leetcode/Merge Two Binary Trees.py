# https://leetcode.com/problems/merge-two-binary-trees/

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

# Time: O(n) | Space: O(height)
def mergeTrees(root1, root2):
    if not root1: return root2
    if not root2: return root1
    root = TreeNode(root1.val + root2.val)
    stack = [(root, root1, root2)]
    while stack:
        r0, r1, r2 = stack.pop()
        if not r1.left or not r2.left:
            r0.left = r1.left if r1.left else r2.left
        else:
            r0.left = TreeNode(r1.left.val + r2.left.val)
            stack.append((r0.left, r1.left, r2.left))
        if not r2.right or not r1.right:
            r0.right = r1.right if r1.right else r2.right
        else:
            r0.right = TreeNode(r1.right.val + r2.right.val)
            stack.append((r0.right, r1.right, r2.right))
    return root

args = (
TreeNode.from_list([1,3,2,5]),
TreeNode.from_list([2,1,3,None,4,None,7])
)
print(mergeTrees(*args))