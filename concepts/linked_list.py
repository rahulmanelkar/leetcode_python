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
        pass

    def return_as_list(self):
        pass


