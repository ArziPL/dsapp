class LinkedList:
    # constructor
    def __init__(self,*args):
        if args != ():
            self.head = Node(args[0])
            for item in args[1:]:
                self.add_last(item)
        else:
            raise SyntaxError("Can't initialize linked list without values")

    # Add at the beginning - O(1) no matter what
    def add_first(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Add at the end - find last node O(n) + add node O(1)
    def add_last(self,data):
        node = Node(data)
        last_node = self.get_last()
        last_node.next = node

    # Add before node at index - worst case O(n)
    # Find node - worst case O(n) (the closer to the end the worse)
    # Add node - O(1)
    def add_before(self,index,data):
        node = Node(data)
        node_befbef = self.get_node(index-1)
        node_after = node_befbef.next
        node_befbef.next = node
        node.next = node_after

    # Add after node at index - O(n)
    # Find node - worst case O(n) (the closer to the end the worse)
    # Add node - O(1)
    def add_after(self,index,data):
        node = Node(data)
        node_before = self.get_node(index)
        node_after = node_before.next
        node_before.next = node
        node.next = node_after

    # Delete node at index - O(n)
    # Find node - worst case O(n) (the closer to end the worse)
    # Delete node - O(1)
    def delete(self,index):
        if index == 0 :
            self.head = self.get_node(index+1)
        node_before = self.get_node(index-1)
        node_after = self.get_node(index+1)
        node_before.next = node_after

    # Get head - O(1)
    def get_first(self):
        return self.head

    # Find node - worst case O(n) (the closer to end the worse)
    def get_node(self,index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    # Get last node - always O(n)
    def get_last(self):
        i_node = self.head
        while i_node is not None:
            current = i_node
            i_node = i_node.next
        return current

    # Print all data in nodes - O(n)
    def print_all(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# # TESTS

# ll = LinkedList(10,20,30)
# ll.add_first(5)
# ll.add_last(40)
# ll.add_after(1,15)
# ll.add_before(4,25)
# ll.delete(3)
# ll.print_all()


