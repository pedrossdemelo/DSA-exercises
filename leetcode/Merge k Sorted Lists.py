# https://leetcode.com/problems/merge-k-sorted-lists/

from idna import valid_contextj


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# n = n of linked lists
# m = average amount of nodes in linked lists
# Time: O(n * m) | Space: O(n * m)
def mergeKLists(lists):
    values = []
    for head in lists:
        while head:
            values.append(head.val)
            head = head.next
    values.sort()
    if not values:
        return None
    head = ListNode(values.pop())
    while values:
        head = ListNode(values.pop(), head)
    return head