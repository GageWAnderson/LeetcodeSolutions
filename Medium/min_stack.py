class MinStackSimple:
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []  # Monotonic decreasing stack top -> bottom

    def push(self, val: int) -> None:
        # NOTE: make basic operations on data structure atomic for ensured consistency
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# NOTE: Linked list was OVERKILL to solve this problem
# Could have just used a monotonic stack instead
# In fact, a monotonic list is literally the exact same thing as a monotonic stack
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: ListNode | None = None
        self.tail: ListNode | None = None

    def is_empty(self) -> bool:
        if (self.head is None and self.tail is not None) or (
            self.tail is None and self.head is not None
        ):
            raise ValueError("List should be empty but head and tail are misaligned")
        return self.head is None

    def push(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self) -> None:
        if not self.tail:
            raise ValueError("Attempted to pop from an empty linked list")
        prev_tail = self.tail
        self.tail = self.tail.prev
        prev_tail.next = None
        prev_tail.prev = None

        if self.tail is None:
            self.head = None

    def get_tail(self) -> int:
        if not self.tail:
            raise ValueError("Called get_tail with an empty linked list")
        return self.tail.value


class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.linked_list = LinkedList()

    def push(self, val: int) -> None:
        # NOTE: make basic operations on data structure atomic for ensured consistency
        if self.linked_list.is_empty() or val <= self.linked_list.get_tail():
            self.linked_list.push(val)
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack or not self.linked_list:
            raise ValueError("Caled pop with an empty stack")
        top = self.stack[-1]
        curr_tail = self.linked_list.get_tail()
        if top == curr_tail:
            self.linked_list.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise ValueError("Called top with an empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        return self.linked_list.get_tail()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
