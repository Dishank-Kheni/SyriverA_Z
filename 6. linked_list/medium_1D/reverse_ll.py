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

    def reverse(self, node):
        if node.next is None:
            self.head = node
            return node
        n = self.reverse(node.next)
        node.next.next = node
        node.next = None
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
    llist = LinkedList([1, 2, 3, 4])
    llist.reverse(llist.head)
    print(llist)
    # llist1 = LinkedList([4, 3, 2, 2, 1])
    # llist2 = LinkedList([3, 1])

    # n1 = Node(6)
    # n2 = Node(7)

    # llist1.add_after(1, n1)
    # llist1.add_after(1, n2)
    # llist2.add_after(1, n1)
    # llist2.add_after(1, n2)

    # print(llist1)
    # print(llist2)

    # llist1.reverse(llist1.head)
    # llist2.reverse(llist2.head)
    # llist.reverse(llist.head)

    # def reverse(node) -> Node:
    #     if node.next is None:
    #         return node
    #     n = reverse(node.next)
    #     n.next = node
    #     return node

    # n = reverse(llist.head)
    # n.next = None
    # print(llist1)
    # print(llist2)
    # print(llist)
