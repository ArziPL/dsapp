class LinkedList:
    # Constructor - return nothing - O(n) of initial arguments
    def __init__(self, *args):
        if args != ():
            self.head = Node(args[0])
            for data in args[1:]:
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
        node.next = self.head
        self.head = node

    # Add at the end - return nothing - find last node O(n) + add node O(1)
    def add_last(self, data):
        node = Node(data)
        last_node = self.get_last()
        last_node.next = node

    # Add before node at index - return nothing - worst case O(n) (the closer to the end the worse) + O(1) adding node
    def add_before(self, index, data):
        if index == 0:
            self.add_first(data)
            return
        node = Node(data)
        node_befbef = self.get_node(index-1)
        node_after = node_befbef.next
        node_befbef.next = node
        node.next = node_after

    # Add after node at index - return nothing - find node worst case O(n) (the closer to the end the worse) + O(1) adding node
    def add_after(self, index, data):
        node = Node(data)
        node_before = self.get_node(index)
        node_after = node_before.next
        node_before.next = node
        node.next = node_after

    # Delete node at index - return nothing - find node worst case O(n) (the closer to the end the worse) + O(1) delete node
    def delete(self, index):
        if index == 0:
            self.head = self.get_node(index+1)
        node_before = self.get_node(index-1)
        node_after = self.get_node(index+1)
        node_before.next = node_after

    # Get first node - return head of list(Node) - O(1)
    def get_first(self):
        return self.head

    # Find node - return node(Node) - worst case O(n) (the closer to end the worse)
    def get_node(self, index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    # Get last node - return last node(Node) - always O(n)
    def get_last(self):
        i_node = self.head
        while i_node is not None:
            current = i_node
            i_node = i_node.next
        return current

    # Find if node with data exists - return index(int) or False - worst case O(n) (the closer to end the worse)
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

# # TESTS

# ll = LinkedList(10,20,30)
# print(ll)
# ll.add_first(5)
# ll.add_last(40)
# ll.add_before(2,15)
# ll.add_after(3,25)
# ll.add_after(0,7)
# ll.add_before(0,2)
# print(ll.search(23))
# ll.traverse()
# print(ll)
