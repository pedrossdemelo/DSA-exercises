# https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


# Time: O(n) | Memory: O(n)
# def isPalindrome(head):
#     if not head or not head.next:
#         return True
#     fast = slow = head
#     stack = []
#     reached_mid = False
#     while slow:
#         if not reached_mid:
#             stack.append(slow.val)
#         else:
#             val = stack.pop()
#             if slow.val != val:
#                 return False
#         slow = slow.next

#         if fast and not reached_mid:
#             if not fast.next:
#                 reached_mid = True
#                 stack.pop()
#             elif fast.next and not fast.next.next:
#                 reached_mid = True
#                 val = stack.pop()
#                 if slow.val != val:
#                     return False
#                 slow = slow.next
#             else:
#                 fast = fast.next.next

#     return True


def reverse(head):
    curr, prev = head, None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head


# Time: O(n) | Memory: O(1)
def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = fast = head

    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None

    right, left = reverse(slow), head

    while right:
        if right.val != left.val:
            return False
        right = right.next
        left = left.next

    return True


head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

print(isPalindrome(head))
