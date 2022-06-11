# https://leetcode.com/problems/reorder-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Time: O(n) | Space: O(1)
def reorderList(head):
    slow = fast = head
    try:
        fast = fast.next.next
    except AttributeError:
        return head
    while fast:
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            break
    mid = slow.next
    slow.next = None
    mid = reverseList(mid)
    start = head
    while mid:
        next_start, next_mid = start.next, mid.next
        start.next, mid.next = mid, next_start
        start, mid = next_start, next_mid

list = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

print(reorderList(list))
print(list)
