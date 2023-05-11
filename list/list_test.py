from linked_list import List
from node import Node

def main() -> None:
    elements_list: list[int] = [12,321,43,43,12,54,123,3412,334,543,-2,23,54]
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
    
    """print("Remove the duplicates of the list")
    
    purge_repeated(list1)
    
    list1.print_list()"""

    print("Elements will be added to list2")
    node = list2.first_item()
    for element in elements_list:
        list2.insert_item(element, node)
        node = list2.next_item(node)

    """print(f"Now the two list will be concatinated --> return value: {list1.add_list(list2)}")
    
    
    list1.print_list()"""
    
    print(f"List1 will be cleared --> return value: {list1.clear_list()}")
    print(f"List1 will be destroyed --> return value: {list1.destroy()}")
    
    print(f"List2 will be cleared --> return value: {list2.clear_list()}")
    print(f"List2 will be destroyed --> return value: {list2.destroy()}")
    
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
    main()
