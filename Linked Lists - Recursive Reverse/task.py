def reverse(head):
    res = None
    while head != None:
        res, head.next, head = head, res, head.next
    return res