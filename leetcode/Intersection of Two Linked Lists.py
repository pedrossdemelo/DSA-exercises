# https://leetcode.com/problems/intersection-of-two-linked-lists/
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

    def __repr__(self) -> str:
        try:
            return f"{self.val} -> {self.next}"
        except RecursionError:
            return "∞"

# n = headA nodes, m = headB nodes
# Time: O(n + m) | Space: O(1)
def getIntersectionNode(headA: ListNode, headB: ListNode):
    slow, fast, connect_node, has_intersection = headA, headA, None, False
    while fast:
        if fast == slow and connect_node:
            has_intersection = True
            break
        if not connect_node and not fast.next:
            connect_node = fast
            fast.next = headB
        elif not connect_node and fast.next and not fast.next.next:
            connect_node = fast.next
            fast.next.next = headB
        slow = slow.next
        fast = fast.next.next if fast.next else None
    if not has_intersection: 
        connect_node.next = None
        return
    fast = headA
    while fast != slow:
        fast = fast.next
        slow = slow.next
    connect_node.next = None
    return fast

intrsct = ListNode(10, ListNode(30))

b = ListNode(8, ListNode(2, ListNode(1, intrsct)))

a = ListNode(2, intrsct)

print(getIntersectionNode(a, b))