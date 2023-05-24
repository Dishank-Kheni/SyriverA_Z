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

    def middelNode(self):
        lenght = self.__len__()
        temp = 0
        for node in self:
            if temp == (lenght//2):
                break
            temp += 1

        return node

    def reverse(self, node):
        if node.next is None:
            self.head1 = node
            return node
        n = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return n
    #     n.next = node
    #     return node

    def isPalindrome(self):
        if self.head is None:
            return False

        middleNode = self.middelNode()
        self.reverse(middleNode)
        print(self.__eq__(self.head1))

    def __eq__(self, node) -> bool:
        headNode = self.head
        while headNode is not None and node is not None:
            if headNode.data != node.data:
                return False
            headNode = headNode.next
            node = node.next
        return True

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def intersection(self, head2):

        self.reverse(self.head)
        # self.reverse(head2)

        # print(self)
        # print(head2)

        # while head1 is not None and head2 is not None:
        #     if head1 == head2:
        #         return head1
        #     head1 = head1.next
        #     head2 = head2.next
        return None


if __name__ == '__main__':

    # Start with the empty list
    llist1 = LinkedList([4, 3, 2, 2, 1])
    llist2 = LinkedList([3, 1])
    # n1 = Node(6)
    # n2 = Node(7)
    # llist1.add_after(1, n1)
    # llist1.add_after(1, n2)
    # llist2.add_after(1, n1)
    # llist2.add_after(1, n2)
    # print(llist)
    # llist.reverse(llist.head)

    # def reverse(node) -> Node:
    #     if node.next is None:
    #         return node
    #     n = reverse(node.next)
    #     n.next = node
    #     return node

    print(llist1)
    llist1.reverse(llist1.head)
    print(llist1)

    # n.next = None
    # print(llist2)
    # llist1.intersection(llist2.head)
    # print(llist1)
    # print(llist2)
