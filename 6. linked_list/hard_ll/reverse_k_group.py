class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def reverseKGroup(self, k):
        if self.head is None:
            raise Exception('List is empty')
        if k == 1:
            return

        length = len(self)

        dummyHead = Node(0)
        dummyHead.next = self.head
        pre = dummyHead
        cur = None
        nex = None

        while length >= k:
            cur = pre.next
            nex = cur.next
            for i in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            length -= k
        self.head = dummyHead.next

        # pre =

    def reverse(self, nd, endNode, count):
        if nd == endNode:
            if count == 1:
                self.head = nd
            return nd
        n = self.reverse(nd.next, endNode, count)
        nd.next.next = nd
        nd.next = None
        return n

    def iterate_rev(self):
        if self.head is None and self.head.next is None:
            return

        prev_node = None
        cur_node = self.head
        nxt_node = None

        while cur_node is not None:
            nxt_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = nxt_node
        self.head = prev_node
        # if node == endNode:
        #     if count == 1:
        #         self.head = node
        #     return node
        # n = self.reverse(node.next, endNode, count)
        # node.next.next = node
        # node.next = None
        # return n
    #     n.next = node
    #     return node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList([1, 2, 3, 4, 5, 6, 7])
    n = Node(3)
    # llist.add_after(3, n)
    # llist.reverse(llist.head, n, 1)
    print(llist)
    # llist.iterate_rev()
    print(llist.reverseKGroup(3))
    print(llist)
