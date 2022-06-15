# https://leetcode.com/problems/all-possible-full-binary-trees/

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self == None:
            return ""
        if self.left == self.right == None:
            return str(self.val)
        ans = str(self.val)
        if self.left != None:
            ans = ans + "(" + str(self.left) + ")"
        else:
            ans = ans + "()"
        if self.right != None:
            ans = ans + "(" + str(self.right) + ")"
        return ans


def allPossibleFBT(n):
    fbts_with = defaultdict(list)
    fbts_with[1].append(TreeNode())

    if n % 2 == 0 or n == 1:
        return fbts_with[n]

    def get_fbts_with(nodes):
        if nodes not in fbts_with:
            child_nodes = nodes - 1
            for left_nodes in range(1, child_nodes, 2):
                right_nodes = child_nodes - left_nodes
                for left_fbt in get_fbts_with(left_nodes):
                    for right_fbt in get_fbts_with(right_nodes):
                        fbts_with[nodes].append(
                            TreeNode(left=left_fbt, right=right_fbt)
                        )

        return fbts_with[nodes]

    return get_fbts_with(n)

print([str(r) for r in allPossibleFBT(11)])