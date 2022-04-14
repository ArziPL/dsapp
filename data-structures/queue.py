class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self,*args):
        self.size = 0
        if args != ():
                for i in args:
                    self.enqueue(i)

    # For print
    def __str__(self):
        self.to_return = []
        i = self.first
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return str(self.to_return)

    # For other prints
    def __repr__(self):
        self.to_return = []
        i = self.first
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return str(self.to_return)
        
    # For length
    def __len__(self):
        return self.size

    # Add item at the end of queue - return nothing - always O(1)
    def enqueue(self,data):
        if self.size == 0:
            self.first = Node(data)
            self.first.next = None
            self.last = self.first
            self.last.next = None
        else:
            self.new_node = Node(data)
            self.last.next = self.new_node
            self.last = self.new_node
        self.size += 1

    # Delete item at the beginning of queue - return nothing - always O(1)
    def dequeue(self):
        if self.size == 0:
           print("It's empty")
        else:
            self.first = self.first.next
        self.size -= 1

    # Check item at the beginning of the queue - return data at the the beginning - always O(1)
    def front(self):
        if self.first is not None:
            print(self.first.data)
            return self.first.data
        else:
            print("It's empty")

    # Traverse the queue - return stack in list - always O(n)
    def traverse(self):
        self.to_return = []
        i = self.first
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return self.to_return
    
    # Return the size - return number of items in queue - always O(1)
    def return_size(self):
        return self.size


# TESTS

# q = Queue("Hello","Its","Test")
# q.enqueue("And")
# q.enqueue("Its")
# q.enqueue("Good")
# print(q.return_size())
# print(q)
# q.front()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.front()
# q.enqueue("Its")
# q.enqueue("Good")
# q.front()
# print(q)
# print(q.return_size())
# print(q.traverse())
# print(len(q))