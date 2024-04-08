from preloaded import Node

def swap_pairs(head):
    if head == None or head.next == None:
        return head
    prev = None
    cur = head
    res = head.next

    while cur and cur.next:
        n_p = cur.next.next

        if prev:
            prev.next = cur.next
        cur.next.next = cur
        cur.next = n_p

        prev = cur
        cur = n_p
    return res