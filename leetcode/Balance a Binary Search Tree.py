# https://leetcode.com/problems/balance-a-binary-search-tree/

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
def balanceBST(root):
    stack, inorder = [], []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        else:
            curr = stack.pop()
        inorder.append(curr.val)
        curr = curr.right
    n = len(inorder)

    def balance(min=0, max=n-1):
        if max < min:
            return None
        mid = (max+min) // 2
        left = balance(min, mid-1)
        right = balance(mid+1, max)
        return TreeNode(inorder[mid], left, right)

    return balance()
root = TreeNode.from_list([2,1,3])
print(balanceBST(root))