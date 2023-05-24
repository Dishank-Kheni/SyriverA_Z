def countNodesinLoop(head):
    if head is None or head.next is None:
        return 0

    slow, fast = head, head
    count = 1

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            while slow.next != fast:
                count += 1
            return count
    return 0
