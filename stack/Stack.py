from typing import Literal
from Node import Node

class Stack:
    def __init__(self) -> None:
        self.head: Node = Node()
        self.head.next = None

    def isEmpty(self) -> bool:
        return self.head is None or self.head.next is None

    def push(self, value: int) -> Literal[-1, 0]:
        if self.head is None:
            return -1
        else:
            node = Node(value)
            node.next = self.head.next
            self.head.next = node
            return 0

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            node: Node = self.head.next
            self.head.next = node.next
            node.next = None
            return node.value

    def __str__(self) -> str:
        temp = []

        curr_node: Node = self.head.next
        while curr_node is not None:
            temp.append(str(curr_node.value))
            curr_node = curr_node.next
        if len(temp) == 0:
            return "Empty"
        
        return '->'.join(temp)