from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if index <0:
        raise Exception
    if not isinstance(node, Node):
        raise Exception
    for _ in range(index):
        try:
            node = node.next
        except:
            raise Exception
    if isinstance(node, Node):
        return node
    raise Exception
  