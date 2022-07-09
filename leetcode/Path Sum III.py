# https://leetcode.com/problems/path-sum-iii/

from collections import defaultdict, deque
from typing import Optional

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


# Time: O(n) | Space: (height of tree)
def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    prefixCount = defaultdict(int)
    prefixCount[0] = 1
    def inc(value):
        prefixCount[value] += 1
    def dec(value):
        prefixCount[value] -= 1
        if prefixCount[value] == 0:
            del prefixCount[value]
    def get(value):
        if value not in prefixCount:
            return 0
        return prefixCount[value]

    pathSums = 0
    def dfs(node, currSum=0):
        nonlocal pathSums
        if not node:
            return
        currSum += node.val
        target = currSum - targetSum
        pathSums += get(target)
        inc(currSum)
        dfs(node.left, currSum)
        dfs(node.right, currSum)
        dec(currSum)

    dfs(root)

    return pathSums

root = TreeNode.from_list([0,None,-8,None,8,None,-8,None,0,None,8,None,8])

print(pathSum(root, 8))