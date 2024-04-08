class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def push(head, data):
    a = Node(data)
    a.next = head
    return a

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    head1 = None
    head2 = None
    tail1 = None
    tail2 = None
    cur = head
    count = 1
    while cur:
        if count % 2 != 0:
            if head1 is None:
                head1 = cur
                tail1 = cur
            else:
                tail1.next = cur
                tail1 = cur
        else:
            if head2 is None:
                head2 = cur
                tail2 = cur
            else:
                tail2.next = cur
                tail2 = cur
        cur = cur.next
        count += 1
    if tail1:
        tail1.next = None
    if tail2:
        tail2.next = None

    return Context(head1, head2)