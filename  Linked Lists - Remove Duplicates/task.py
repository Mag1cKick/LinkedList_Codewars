class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head == None:
        return None
    listok = []
    while head != None:
        listok.append(head.data)
        head=head.next
    listok = sorted(list(set(listok)))[::-1]
    b = Node(listok[0])
    for i in range(1, len(listok)):
        b = push(b, listok[i])
    return b
        