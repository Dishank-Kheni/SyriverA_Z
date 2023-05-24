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

    def removeNodeFromBack(self, n):
        length = len(self)
        count = 1
        headNode = self.head
        while count < length-n:
            headNode = headNode.next
            count += 1

        headNode.next = headNode.next.next

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


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList([1, 2, 3, 2, 1])
    # print(llist)
    # llist.reverse(llist.head)

    # def reverse(node) -> Node:
    #     if node.next is None:
    #         return node
    #     n = reverse(node.next)
    #     n.next = node
    #     return node

    # n = reverse(llist.head)
    # n.next = None
    llist.removeNodeFromBack(2)

    print(llist)
