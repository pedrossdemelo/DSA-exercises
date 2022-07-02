# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from heapq import heappush


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr, i=0):
        root = None
        if i < len(arr) and arr[i] is not None:
            root = cls(arr[i])
            root.left = cls.from_list(arr, 2 * i + 1)
            root.right = cls.from_list(arr, 2 * i + 2)

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

root = TreeNode.from_list([3,1,4,3,None,1,5])

# Time: O(n) | Space: O(1)
def goodNodes(root):
    result = 0
    maxseen = float('-inf')

    def dfs(node):
        nonlocal maxseen, result
        if not node: return
        oldmax = maxseen
        if node.val >= maxseen:
            result += 1
            maxseen = node.val
        dfs(node.left)
        dfs(node.right)
        maxseen = oldmax

    dfs(root)
    return result


print(goodNodes(root))