#Linked List Implementation in python
from typing import Any
class Node:
    def __init__(self, data:Any, next=None, prev=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        node = Node(data, next = self.head)
        self.head = node

    def insert_at_end(self,data):
        pass

    def insert_at(self,data):
        pass

    def remove_at(self,data):
        pass

    def insert_values(self,values):
        pass

    def print(self):
        node = self.head
        if node is None:
            print("Empty")
            return
        ll_text = ''
        while node:
            ll_text += str(node.data) + '-->'
            node = node.next

        print(ll_text)
        return 

    def return_as_list(self):
        pass


if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(35)
    ll.insert_at_beginning(54)
    ll.print()