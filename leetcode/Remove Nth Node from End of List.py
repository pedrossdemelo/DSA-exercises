class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val} -> {self.next}"

def removeNthFromEnd(head, n):
    slow = fast = head
    listlen = curr_i = 0

    while fast:
        curr_i += 1
        slow = slow.next
        try:
            fast = fast.next.next
        except AttributeError:
            listlen = curr_i * 2 - 1
            break

    if listlen == 0:
        listlen = curr_i * 2
    if listlen == 1:
        return None

    target_i = listlen - n
    if target_i == 0:
        head = head.next
        return head

    distance = target_i - curr_i
    if distance <= 0:
        slow = head
        distance = listlen - n
    while distance != 1:
        distance -= 1
        slow = slow.next
    slow.next = slow.next.next
    return head

list = ListNode(4, ListNode(5, ListNode(6)))
list2 = ListNode(1, ListNode(2, ListNode(3, list)))

print(removeNthFromEnd(ListNode(), 2))
