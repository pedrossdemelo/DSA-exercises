# https://leetcode.com/problems/linked-list-cycle/

def hasCycle(head):
    if not head.next or not head.next.next:
        return False

    thing = head

    slow = head.next
    fast = head.next.next

    while slow and fast:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next if fast.next else None

    return False

class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __str__(self):
        if hasCycle(self):
            return "Infinite loop"

        return f"{hex(id(self))} -> {self.next}"

link = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))

link.next.next.next.next = link
print(link)
print(hasCycle(link))
