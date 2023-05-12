from linked_list import List
from node import Node
import random

def main(size: int) -> None:
    elements_list: list[int] = list()
    for i in range(size):
        elements_list.append(random.randint(1, 100))
    
    list1: List = List()
    list2: List = List()
    node: Node
    print(f"Create the empty list1 --> return value: {list1.createEmpty()}")
    print(f"Create the empty list2 --> return value: {list2.createEmpty()}")
    
    node = list1.first_item()
    
    print("Elements will be added to list1")
    for element in elements_list:
        list1.insert_item(element, node)
        node = list1.next_item(node)
        
    print("Elements added, now will be displayed")
    list1.print_list()
    while 1:
        try:
            temp = int(input("Give a number to find if in the linked list: "))
            break
        except ValueError as e:
            print("Introduce an integer please")

    print(f"Is {temp} in the linked list? --> return value: {list1.search_item(temp)}")

    print("Elements will be added to list2")
    node = list2.first_item()
    random.shuffle(elements_list)
    for element in elements_list:
        list2.insert_item(element, node)
        node = list2.next_item(node)

    list2.print_list()
    
    print(list1.add_list(list2))

    print(id(list1.last_node.next))
    
def purge_repeated(list: List):
    node: Node
    aux: Node
    
    node = list.first_item()
    while(node != list.last_item()):
        aux = list.next_item(node)
        while aux != list.last_item():
            if list.get_value(aux) == list.get_value(node):
                res = list.delete_item(aux)
            else:
                aux = list.next_item(aux)
        node = list.next_item(node)    
        
if __name__ == '__main__':
    while 1:
        try:
            size = int(input("How many objects do you want in the linked list? "))
            break
        except ValueError as e:
            print("You don't introduce a valid value")
    
    main(size)