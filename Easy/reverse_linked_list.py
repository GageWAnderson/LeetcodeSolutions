import random
from typing import Any

NUM_TEST_CASES = 100
LL_SIZE = 10
LL_MIN = -100
LL_MAX = 100


class ListNode:
    def __init__(self, val: Any):
        self.prev: ListNode | None = None
        self.next: ListNode | None = None
        self.value = val


class LinkedList:
    def __init__(self, input_array: list[Any]):
        self.head = None
        self.tail = None
        curr_node: ListNode | None = None
        prev_node: ListNode | None = None
        for i in range(len(input_array)):
            curr_node = ListNode(val=input_array[i])
            curr_node.prev = prev_node
            if prev_node:
                prev_node.next = curr_node
            if i == 0:
                self.head = curr_node
            prev_node = curr_node
        if prev_node:
            prev_node.next = None
        self.tail = curr_node

    def reverse(self) -> None:
        prev_node = None
        next_node = None
        curr_node = self.head
        self.tail = self.head
        while curr_node:
            next_node = curr_node.next
            prev_node = curr_node.prev
            curr_node.next = prev_node
            curr_node.prev = next_node
            curr_node = next_node
        if prev_node and prev_node.prev:
            self.head = prev_node.prev

    def detect_cycle(self) -> bool:
        slow = self.head
        fast = self.head.next if self.head else None
        while slow:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast and fast.next else None
        return False

    def to_list(self) -> list[Any]:
        curr_node = self.head
        res: list[ListNode] = []
        while curr_node:
            res.append(curr_node)
            curr_node = curr_node.next
        return [node.value for node in res]

    def __repr__(self):
        curr_node = self.head
        res: list[ListNode] = []
        while curr_node:
            res.append(curr_node)
            curr_node = curr_node.next
        return "->".join([str(node.value) for node in res])


def get_test_cases() -> list[LinkedList]:
    test_cases = []
    for _ in range(NUM_TEST_CASES):
        input_array = [
            random.randint(LL_MIN, LL_MAX) for _ in range(random.randint(0, LL_SIZE))
        ]
        test_cases.append(LinkedList(input_array))
    return test_cases


def check_list_deepequal(l1: list[Any], l2: list[Any]) -> bool:
    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


def main():
    test_cases = get_test_cases()
    for test_case_ll in test_cases:
        forward = test_case_ll.to_list()
        print(f"Forward: {test_case_ll.to_list()}")
        test_case_ll.reverse()
        reverse = test_case_ll.to_list()
        print(f"Reversed: {test_case_ll.to_list()}")
        reverse_of_reverse = list(reversed(reverse))
        assert check_list_deepequal(forward, reverse_of_reverse)
    print("All tests passed! You passed an easy LC problem!")


if __name__ == "__main__":
    main()
