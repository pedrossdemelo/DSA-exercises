# https://leetcode.com/problems/increasing-order-search-tree/

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
def increasingBST(root: TreeNode) -> TreeNode:
    curr, stack = root, []
    sentinel = TreeNode()
    skewed = sentinel
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        skewed.right = TreeNode(curr.val)
        skewed = skewed.right
        curr = curr.right
    return sentinel.right

root = TreeNode.from_list([5,3,6,2,4,None,8,1,None,None,None,7,9])

print(increasingBST(root))