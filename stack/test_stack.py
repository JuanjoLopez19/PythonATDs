from Stack import Stack
from node import Node
import random

def main(size: int) -> None:
    elements_list: list[int] = list()
    for i in range(size):
        elements_list.append(random.randint(1, 100))
    stack = Stack()
    
    for temp in elements_list:
        stack.push(temp)
    
    print(stack)
    while not stack.isEmpty():
        print(f"Value extracted: {stack.pop()}")
    
    print(f"Now the stack is empty --> return value {stack.isEmpty()}")
    print(f"Stack --> {stack}")
if __name__ == '__main__':
    while 1:
        try:
            size = int(input("How many objects do you want in the stack? "))
            break
        except ValueError as e:
            print("You don't introduce a valid value")
    
    main(size)