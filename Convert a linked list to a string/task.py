class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    if node == None: 
        return 'None'
    elif node.next == None:
        return str(node.data) + ' -> None'
    else:
        return str(node.data) + ' -> ' + stringify(node.next)
