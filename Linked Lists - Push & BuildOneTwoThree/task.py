from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    a = Node(data)
    a.next = head
    return a

def build_one_two_three():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    c.next = None
    b.next = c
    a.next = b
    return a