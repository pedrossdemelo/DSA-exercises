# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class FindElements:
    # Time: O(n) | Space: (height of tree)
    def __init__(self, root):
        self.values = {0}
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            leftval, rightval = node.val * 2 + 1, node.val * 2 + 2
            if node.left:
                self.values.add(leftval)
                node.left.val = leftval
                stack.append(node.left)
            if node.right:
                self.values.add(rightval)
                node.right.val = rightval
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values