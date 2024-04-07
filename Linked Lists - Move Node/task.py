class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    a = Node(source.data)
    a.next = dest
    dest = a
    source = source.next
    return Context(source, dest)