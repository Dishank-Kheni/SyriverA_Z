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


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList([1, 2, 3, 4])
    print(llist)
    print(llist.middelNode())
