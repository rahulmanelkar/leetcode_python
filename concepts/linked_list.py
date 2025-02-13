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
        self.currentstate_text = ''

    def insert_at_beginning(self,data):
        node = Node(data, next = self.head)
        self.head = node
        if not self.tail:
            self.tail = node

    def insert_at_end(self,data):
        pass
          

    def insert_at(self,data):
        pass

    def remove_at(self,data):
        pass

    def insert_values(self,values):
        for i in values:
            self.insert_at_beginning(i)

    def current_state(self):
        node = self.head
        if node is None:
            print("Empty")
            return
        ll_text = ''
        while node:
            ll_text += str(node.data) + '-->'
            node = node.next

        self.currentstate_text = ll_text
        return self.currentstate_text

    def print(self):
        self.current_state()
        print(self.currentstate_text)
        return 

    def return_as_list(self):
        node = self.head
        if node is None:
            return None
        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next

        return ll_list


if __name__=='__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(25)
    ll.insert_at_beginning(35)
    ll.insert_at_beginning(54)
    ll.print()