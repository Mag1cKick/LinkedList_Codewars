""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head == None:
        return Node(data)
    if data >= head.data:
        head.next = sorted_insert(head.next, data)
        return head
    else:
        a = Node(data)
        a.next = head
        return a