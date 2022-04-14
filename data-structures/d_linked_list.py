class DLinkedList:
    # Constructor - return nothing - O(n) of initial arguments
    def __init__(self, *args):
        if args != ():
            self.size = len(args)
            self.head = Node(args[0])
            if len(args) == 2:
                self.tail = Node(args[-1])
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                self.head = Node(args[0])
                middle = Node(args[1])
                self.tail = Node(args[2])
                self.head.next = middle
                middle.next = self.tail
                middle.prev = self.head
                self.tail.prev = middle
                for data in args[3:]:
                    self.add_last(data)

        else:
            raise SyntaxError("Can't initialize linked list without values")
    

    # For print
    def __str__(self):
        this_list = []
        node = self.head
        while node is not None:
            this_list.append(node.data)
            node = node.next
        return str(this_list)

    # For other prints
    def __repr__(self):
        this_list = []
        node = self.head
        while node is not None:
            this_list.append(node.data)
            node = node.next
        return str(this_list)

    # Add at the beginning - return nothing - O(1) no matter what
    def add_first(self, data):
        node = Node(data)
        old_head = self.head
        node.next = old_head
        old_head.prev = node
        self.head = node
        self.size += 1

    # Add at the end - return nothing - O(1) => find last node O(1) + add node O(1)
    def add_last(self, data):
        node = Node(data)
        last_node = self.get_last()
        last_node.next = node
        node.prev = last_node
        self.tail = node
        self.size += 1

    # Add before at index - return nothing - O(n) => find node O(1/2n) (the closer to half of list the worse) + O(1) adding node
    def add_before(self, index, data):
        if index == 0:
            self.add_first(data)
            return
        node = Node(data)
        node_at_index = self.get_node(index)
        node_bef = self.get_node(index-1)
        node.next = node_at_index
        node.prev = node_bef
        node_bef.next = node
        node_at_index.prev = node
        self.size += 1

    # Add after at index - return nothing - O(n) => find node O(1/2n) (the closer to half of list the worse) + O(1) adding node
    def add_after(self, index, data):
        node = Node(data)
        node_at_index = self.get_node(index)
        node_after = self.get_node(index+1)
        node.prev = node_at_index
        node.next = node_after
        node_at_index.next = node
        node_after.prev = node
        self.size += 1

    # Delete node at index - return nothing - O(n) => finde node O(1/2n) (the closer to half of list the worse) + O(1) delete node
    def delete(self, index):
        if index == 0:
            self.head = self.get_node(index+1)
            self.head.prev = None
            return
        node_before = self.get_node(index-1)
        node_after = self.get_node(index+1)
        node_before.next = node_after
        node_after.prev = node_before
        self.size -= 1

    # Get first node - return head of list(node) - O(1)
    def get_first(self):
        return self.head

    # Find node - return node(node) - O(n) => find node O(1/2n) (closer to half of the list the worse)
    def get_node(self, index):
        if index > 0.5 * self.size:
            node = self.tail
            for i in range(index):
                node = node.prev
            return node
        elif index <= 0.5 * self.size:
            node = self.head
            for i in range(index):
                node = node.next
            return node

    # Get last node - return tail of list(node) - O(1)
    def get_last(self):
        return self.tail

    # Find if node with data exists - return index(int) or False - O(n) => find node O(1/2n) (closer to half of the list the worse)
    def search(self, data):
        i_node = self.head
        index = 0
        while i_node is not None:
            if i_node.data == data:
                return index
            i_node = i_node.next
            index += 1
        return False

    # Traverse the list - print the list - O(n)
    def traverse(self):
        node = self.head
        while node is not None:
            print(f"{node.data}", end=" ---> ")
            node = node.next

    # Traverse the list in reverse / from the end - print the list - O(n)
    def reverse_traverse(self):
        node = self.tail
        while node is not None:
            print(f"{node.data}", end=" ---> ")
            node = node.prev

    # All nodes to one list - return list with nodes(list of nodes) - O(n)
    def return_all_nodes(self):
        all_nodes = []
        node = self.head
        while node is not None:
            all_nodes.append(node)
            node = node.next
        return all_nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# TESTS
# NEED REWRITE

# ll = DLinkedList(10, 20, 30, 40, 50)
# print(ll)
# print(ll.return_all_nodes())
# ll.add_first(5)
# ll.add_last(60)
# ll.add_before(2, 15)
# ll.add_before(4, 25)
# ll.add_after(1, 12)
# ll.add_after(5, 27)
# ll.add_before(0, 2)
# ll.delete(0)
# ll.delete(4)
# print(ll.search(15))
# ll.traverse()
# print("\n")
# ll.reverse_traverse()
