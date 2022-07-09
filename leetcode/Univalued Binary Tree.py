# https://leetcode.com/problems/univalued-binary-tree/submissions/

# Time: O(n) | Space: O(height)
def isUnivalTree(root):
    stack, last = [root], root.val
    while stack:
        curr = stack.pop()
        if not curr: continue
        if curr.val != last:
            return False
        stack.append(curr.left)
        stack.append(curr.right)
    return True