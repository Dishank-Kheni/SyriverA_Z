# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def __repr__(self):
        return str(self.data)

# Linked List class


class LinkedList:

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
                node = node.next
            # self.head = None

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

    def add_between(self, existNode, newNode):
        newNode.next = existNode.next
        existNode.next = newNode

    def remove_node(self, removeKey):
        temp = self.head
        while temp is not None:
            if temp.data == removeKey:
                break

    # This function prints contents of linked list
    # starting from head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # def __iter__(self):
    #     node = self.head
    #     while node is not None:
    #         yield node
    #         node = node.next


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList([1, 2, 3, 4])
    # llist = LinkedList([1])

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second  # Link first node with second
    # second.next = third  # Link second node with the third node
    llist.add_first(node=Node(7))
    llist.add_last(node=Node(6))
    # llist.add_between(existNode=third, newNode=Node(15))
    # llist.printList()
    print(llist)

    for node in llist:
        print(node)
    # print(llist.__iter__())
