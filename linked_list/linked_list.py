import copy
from Node import Node
from typing import Union


class List:
    def __init__(self):
        self.root: Node = None
        self.last_node: Node = None

    def createEmpty(self) -> None:
        self.root: Node = Node(-1)
        self.last_node: Node = Node(-1)
        self.root.next: Node = None
        return 0

    def isEmpty(self) -> int:
        if self.root.next is None:
            return 1
        else:
            return 0

    def destroy(self) -> int:
        if self.root.next is not None:
            return -1
        else:
            self.root = None
            self.last_node = None
            return 0

    def print_list(self) -> None:
        if self.root is None:
            return None
        else:
            index: int = 1
            node: Node = self.root.next
            while node is not None:
                print(f"Value {node.value} in position {index}")
                index += 1
                node = node.next

            print(f"List length: {index-1}")

    def first_item(self) -> Union[Node, None]:
        if self.root is None:
            return None
        else:
            return self.root

    def last_item(self) -> Union[Node, None]:
        if self.root is None or self.last_node is None:
            return None
        else:
            return self.last_node

    def insert_item(self, value, node: Node) -> int:
        if self.root is None or node is None:
            return -1
        else:
            temp = Node(value)
            temp.next = node.next
            node.next = temp
            if node is self.last_item():
                self.last_node = temp
            return 0

    def delete_item(self, node: Node) -> int:
        if self.root is None or node is None:
            return -1
        else:
            temp: Node = node.next
            node.next = temp.next
            if node.next is None:
                self.last_node = node
            temp.next = None
            return 0

    def next_item(self, node: Node) -> Union[Node, None]:
        if self.root is None or node is None:
            return None
        else:
            if node is self.last_item():
                return self.last_item()
            else:
                return node.next

    def search_item(self, value) -> Union[Node, None]:
        if self.root is None:
            return None
        else:
            temp: Node = self.root
            while temp.next is not None:
                if temp.next.value == value:
                    return temp.next
                temp = temp.next
            return self.last_item()

    def get_value(self, node: Node) -> int:
        if self.root is None or node is None:
            return -1
        else:
            if node is self.last_item():
                return -2
            else:
                return node.next.value

    def clear_list(self) -> int:
        if self.root is None:
            return -1
        else:
            temp: Node = self.root.next
            aux: Node
            while temp is not  None:
                aux = temp
                temp = temp.next
                aux.next = None
            self.root.next = None
            self.last_node = self.root

            return 0

    def add_list(self, aux_list: "List") -> None:
        if aux_list.isEmpty() or aux_list.root is None:
            return -1

        if self.isEmpty():
            self.root = aux_list.root
            self.last_node = aux_list.last_node
            return 1
        else:
            self.last_node.next = aux_list.first_item()
            return 2
