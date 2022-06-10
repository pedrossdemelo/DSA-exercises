# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n) | Space: O(n)
def mergeTwoLists(list1, list2):
    arr = []
    while list1 or list2:
        if list1:
            arr.append(list1.val)
            list1 = list1.next
        if list2:
            arr.append(list2.val)
            list2 = list2.next
    arr.sort()
    head = None
    while arr:
        head = ListNode(arr.pop(), head)
    return head