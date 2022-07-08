# https://leetcode.com/problems/maximum-width-of-binary-tree/

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


# Time: O(n) | Space: O(w)
def widthOfBinaryTree(root):
    queue = deque([(root, 0, 0)])
    maxwidth = 0
    start = end = currlevel = 0
    while queue:
        node, index, level = queue.popleft()
        if level > currlevel:
            maxwidth = max(maxwidth, 1 + end - start)
            currlevel = level
            start = index
        end = index
        if node.left:
            queue.append((node.left, index * 2 + 1, level+1))
        if node.right:
            queue.append((node.right, index * 2 + 2, level+1))
    maxwidth = max(maxwidth, 1 + end - start)
    return maxwidth

root = TreeNode.from_list([1,3,2,5,None,None,9,None,None,7])
print(widthOfBinaryTree(root))