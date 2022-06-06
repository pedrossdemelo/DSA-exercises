# https://leetcode.com/problems/sort-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def sortList(head):
    l = []
    temp = dummy = head

    while temp:
        l.append(temp.val)
        temp = temp.next

    l.sort()
    # dummy serves to mutate all the values in head using a reference to each
    # node in the linked list
    for i in l:
        dummy.val = i
        dummy = dummy.next

    return head


list = ListNode(3, ListNode(1, ListNode(2, ListNode(9))))

print(list)
print(sortList(list))
