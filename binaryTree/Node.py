class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: TreeNode = None
        self.rigth: TreeNode = None

    def __str__(self) -> str:
        return f"{self.value}"