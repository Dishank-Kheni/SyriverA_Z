def detectCycle(self, head):
    if head is None or head.next is None:
        return -1

    fast, slow, entry = head, head, head
    count = 0

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
                count += 1
            return count

    return -1
