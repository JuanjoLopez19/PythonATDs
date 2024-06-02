class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.next: Node = None

    def __str__(self) -> str:
        return f"Value {self.value}"