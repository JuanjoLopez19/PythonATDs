from Node import Node
class Queue:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def isEmpty(self) -> bool:
        return self.head is None and self.tail is None

    def push(self, value: int) -> int:
        temp: Node = Node(value)
        temp.next = None
        if self.isEmpty():
            self.tail = temp
            self.head = temp
        else:
            self.tail.next = temp
            self.tail = temp
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            temp: Node = self.head
            value: int = temp.value
            self.head = temp.next
            if self.head == None:
                self.head = self.tail = None
            return value

    def __str__(self) -> str:
        temp = []

        curr_node: Node = self.head
        while curr_node is not None:
            temp.append(str(curr_node.value))
            curr_node = curr_node.next
        if len(temp) == 0:
            return "Empty"
        
        return '->'.join(temp)