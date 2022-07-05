# https://leetcode.com/problems/same-tree/

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
def isSameTree(p, q):
    if not p or not q:
        return p == q
    queue = deque([(p, q)])
    try:
        while queue:
            nodep, nodeq = queue.popleft()
            if nodep.val != nodeq.val:
                raise Exception("Not the same XD")
            if nodep.left or nodeq.left:
                queue.append((nodep.left, nodeq.left))
            if nodep.right or nodeq.right:
                queue.append((nodep.right, nodeq.right))
    except Exception:
        return False
    return True

p = TreeNode.from_list([1])
q = TreeNode.from_list([1,None,2])
print(isSameTree(p, q))