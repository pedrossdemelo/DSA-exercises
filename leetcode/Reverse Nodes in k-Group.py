# https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

# Time: O(n) | Space: O(1)
def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def reverseKGroup(head, k):
    steps, curr_head, curr_tail, last_tail = 1, head, head, None
    while curr_tail:
        curr_tail = curr_tail.next
        if not curr_tail: break
        steps += 1
        if steps == k:
            temp = curr_tail.next
            curr_tail.next = None
            curr_tail = curr_head
            curr_head = reverseList(curr_head)
            curr_tail.next = temp
            if not last_tail:
                last_tail = curr_tail
                head = curr_head
            else:
                last_tail.next = curr_head
                last_tail = curr_tail
            curr_tail = curr_head = temp
            steps = 1
    return head

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(reverseKGroup(list, 2))
