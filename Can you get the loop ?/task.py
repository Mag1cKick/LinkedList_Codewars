def loop_size(node):
    if not node:
        return 0
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return 0
    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1
    return count