# https://leetcode.com/problems/design-circular-deque/

class DLLNode:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val, self.prev, self.next = val, prev, next

    def __repr__(self) -> str:
        try:
            prev = "" if self.prev else "None <- "
            next = f" <-> {self.next}" if self.next else " -> None"
            return prev + f"{self.val}" + next
        except RecursionError:
            return "∞"

class MyCircularDeque:
    def __init__(self, k: int):
        self.cap, self.len = k, 0
        self.head_sentinel, self.tail_sentinel = DLLNode(), DLLNode()
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.prev = self.head_sentinel

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.len += 1
        head = self.head_sentinel.next
        newhead = DLLNode(value, self.head_sentinel, head)
        self.head_sentinel.next = head.prev = newhead
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.len += 1
        tail = self.tail_sentinel.prev
        newtail = DLLNode(value, tail, self.tail_sentinel)
        self.tail_sentinel.prev = tail.next = newtail
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.len -= 1
        self.head_sentinel.next = self.head_sentinel.next.next
        self.head_sentinel.next.prev = self.head_sentinel
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.len -= 1
        self.tail_sentinel.prev = self.tail_sentinel.prev.prev
        self.tail_sentinel.prev.next = self.tail_sentinel
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.head_sentinel.next.val

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail_sentinel.prev.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.cap

deque = MyCircularDeque(4)

methods, args = (
["insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"]
,
[[9],[],[],[],[],[],[6],[5],[9],[],[6]]
)

for method, arg in zip(methods, args):
    getattr(deque, method)(*arg)