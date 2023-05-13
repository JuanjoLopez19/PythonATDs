from queue import Queue
from Node import Node
import random

def main(size: int) -> None:
    elements_list: list[int] = list()
    for i in range(size):
        elements_list.append(random.randint(1, 100))
    qeue = Queue()
    
    for temp in elements_list:
        qeue.push(temp)
    
    print(qeue)
    while not qeue.isEmpty():
        print(f"Value extracted: {qeue.pop()}")
    
    print(f"Now the queue is empty --> return value {qeue.isEmpty()}")
    print(f"Stack --> {qeue}")
if __name__ == '__main__':
    while 1:
        try:
            size = int(input("How many objects do you want in the queue? "))
            break
        except ValueError as e:
            print("You don't introduce a valid value")
    
    main(size)