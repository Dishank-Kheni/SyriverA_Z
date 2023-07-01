# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None

    def __repr__(self):
        return str(self.data)

# Linked List class


class DoublyLinkedList:

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
    # Function to initialize the Linked
    # List object

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node.next.prev = node
                node = node.next
            # self.head = None

    def deleteAllOccurOfX(self, key):
        if self.head is None:
            raise Exception("List is empty")

        while self.head.data == key:
            self.head = self.head.next

        previous_node = self.head
        for node in self:
            if node.data == key:
                previous_node.next = node.next
            else:
                previous_node = node

        # raise Exception("Node with data '%s' not found" % key)

    def reverse(self):
        pass

    def findPairsWithGivenSum(self, sum):
        pass

    def removeDuplicates(self):
        if self.head is None:
            raise Exception("List is empty")

        previous_node = self.head
        for node in self:
            if node.data == previous_node.data:
                previous_node.next = node.next
            else:
                previous_node = node

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        pre_node = self.head
        for node in self:
            if node.data == target_node_data:
                pre_node.next = new_node
                new_node.next = node
                return
            pre_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    # def add_between(self, existNode, newNode):
    #     newNode.next = existNode.next
    #     existNode.next = newNode

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # This function prints contents of linked list
    # starting from head

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def middelNode(self):
        lenght = self.__len__()
        temp = 0
        for node in self:
            if temp == (lenght//2):
                break
            temp += 1

        return node

    def get_last_node(self):
        for current_node in self:
            pass
        return current_node

    def findPairsWithGivenSum(self, target):
        pairs = []
        start = self.head
        end = self.get_last_node()

        while start.next is not None and end.prev is not None and start.data <= end.data:
            total = start.data + end.data
            if total > target:
                end = end.prev
                continue
            elif total < target:
                start = start.next
                continue
            else:
                pairs.append((start.data, end.data))
                start = start.next
        return pairs
    # def __iter__(self):
    #     node = self.head
    #     while node is not None:
    #         yield node
    #         node = node.next


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    # llist = DoublyLinkedList([1, 2, 4, 5, 6, 8, 9])
    # llist = DoublyLinkedList([1, 5, 6])
    llist = DoublyLinkedList([1, 1, 1, 2, 3, 4, 5, 6])
    # llist = LinkedList([1])

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second  # Link first node with second
    # second.next = third  # Link second node with the third node
    # llist.add_first(node=Node(7))
    # llist.add_last(node=Node(6))
    # llist.add_between(existNode=third, newNode=Node(15))
    # llist.printList()

    # llist.deleteAllOccurOfX(2)
    # print(llist.findPairsWithGivenSum(6))
    llist.removeDuplicates()
    print(llist)

    # for node in llist:
    #     print(node)

    # print(llist.middelNode())

    # print(llist.__iter__())
