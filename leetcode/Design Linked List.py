# https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val, self.next = val, next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


class MyLinkedList:
    def __init__(self):
        self.len = 0
        self.head = self.tail = None

    # O(n)
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        return self.get_node(index).val

    # O(n)
    def get_node(self, index: int) -> ListNode:
        if index >= self.len:
            raise IndexError(f"No node at index {index}")
        if index == self.len - 1:
            return self.tail
        else:
            curr, curr_i = self.head, 0
            while curr_i != index:
                curr, curr_i = curr.next, curr_i + 1
            return curr

    # O(1)
    def addAtHead(self, val: int) -> None:
        if self.len == 0:
            self.head = self.tail = ListNode(val)
        else:
            head = ListNode(val, self.head)
            self.head = head
        self.len += 1

    # O(1)
    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.head = self.tail = ListNode(val)
        else:
            tail = ListNode(val)
            self.tail.next = tail
            self.tail = tail
        self.len += 1

    # O(n)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            node_before = self.get_node(index - 1)
            node_before.next = ListNode(val, node_before.next)
            self.len += 1

    # O(n)
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        elif index == 0:
            self.head = self.head.next
            if self.len == 1:
                self.tail = None
        else:
            node_before = self.get_node(index - 1)
            node_before.next = node_before.next.next
            if index == self.len - 1:
                self.tail = node_before
        self.len -= 1

    def __repr__(self) -> str:
        return str(self.head)


def truelen(head):
    len = 0
    while head:
        head = head.next
        len += 1
    return len


mll = MyLinkedList()

methods = [
    "addAtHead",
    "addAtTail",
    "addAtTail",
    "get",
    "get",
    "addAtTail",
    "addAtIndex",
    "addAtHead",
    "addAtHead",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "get",
    "addAtHead",
    "addAtHead",
    "addAtIndex",
    "addAtIndex",
    "addAtHead",
    "addAtTail",
    "deleteAtIndex",
    "addAtHead",
    "addAtHead",
    "addAtIndex",
    "addAtTail",
    "get",
    "addAtIndex",
    "addAtTail",
    "addAtHead",
    "addAtHead",
    "addAtIndex",
    "addAtTail",
    "addAtHead",
    "addAtHead",
    "get",
    "deleteAtIndex",
    "addAtTail",
    "addAtTail",
    "addAtHead",
    "addAtTail",
    "get",
    "deleteAtIndex",
    "addAtTail",
    "addAtHead",
    "addAtTail",
    "deleteAtIndex",
    "addAtTail",
    "deleteAtIndex",
    "addAtIndex",
    "deleteAtIndex",
    "addAtTail",
    "addAtHead",
    "addAtIndex",
    "addAtHead",
    "addAtHead",
    "get",
    "addAtHead",
    "get",
    "addAtHead",
    "deleteAtIndex",
    "get",
    "addAtHead",
    "addAtTail",
    "get",
    "addAtHead",
    "get",
    "addAtTail",
    "get",
    "addAtTail",
    "addAtHead",
    "addAtIndex",
    "addAtIndex",
    "addAtHead",
    "addAtHead",
    "deleteAtIndex",
    "get",
    "addAtHead",
    "addAtIndex",
    "addAtTail",
    "get",
    "addAtIndex",
    "get",
    "addAtIndex",
    "get",
    "addAtIndex",
    "addAtIndex",
    "addAtHead",
    "addAtHead",
    "addAtTail",
    "addAtIndex",
    "get",
    "addAtHead",
    "addAtTail",
    "addAtTail",
    "addAtHead",
    "get",
    "addAtTail",
    "addAtHead",
    "addAtTail",
    "get",
    "addAtIndex",
]
args = [
    [84],
    [2],
    [39],
    [3],
    [1],
    [42],
    [1, 80],
    [14],
    [1],
    [53],
    [98],
    [19],
    [12],
    [2],
    [16],
    [33],
    [4, 17],
    [6, 8],
    [37],
    [43],
    [11],
    [80],
    [31],
    [13, 23],
    [17],
    [4],
    [10, 0],
    [21],
    [73],
    [22],
    [24, 37],
    [14],
    [97],
    [8],
    [6],
    [17],
    [50],
    [28],
    [76],
    [79],
    [18],
    [30],
    [5],
    [9],
    [83],
    [3],
    [40],
    [26],
    [20, 90],
    [30],
    [40],
    [56],
    [15, 23],
    [51],
    [21],
    [26],
    [83],
    [30],
    [12],
    [8],
    [4],
    [20],
    [45],
    [10],
    [56],
    [18],
    [33],
    [2],
    [70],
    [57],
    [31, 24],
    [16, 92],
    [40],
    [23],
    [26],
    [1],
    [92],
    [3, 78],
    [42],
    [18],
    [39, 9],
    [13],
    [33, 17],
    [51],
    [18, 95],
    [18, 33],
    [80],
    [21],
    [7],
    [17, 46],
    [33],
    [60],
    [26],
    [4],
    [9],
    [45],
    [38],
    [95],
    [78],
    [54],
    [42, 86],
]

for method, arg in zip(methods, args):
    try:
        print(mll)
        getattr(mll, method)(*arg)
        trulen = truelen(mll.head)
        if trulen != mll.len:
            print(f"DISCREPANCY! lenght: {mll.len} | true length: {trulen}")
            print(f"method called: {method}(" + ", ".join([str(a) for a in arg]) + ")")
    except Exception as e:
        print(f"ERROR AT: {method}(" + ", ".join([str(a) for a in arg]) + ")")
        print(mll)
        print(e)
        break
