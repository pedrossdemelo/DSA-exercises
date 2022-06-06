# https://leetcode.com/problems/linked-list-cycle-ii/

def detectCycle(head):
    if not head:
        return None

    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    slow2 = head

    while slow2 != slow:
        slow2 = slow2.next
        slow = slow.next

    return slow


class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __str__(self):
        cycle_at = detectCycle(self)
        if cycle_at:
            return f"Error: Cycle at {hex(id(cycle_at))}"
        return f"{self.val} -> {self.next}"


link = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))

link.next.next.next.next = link
new_link = ListNode(69, ListNode(10, link))

print(detectCycle(new_link))
