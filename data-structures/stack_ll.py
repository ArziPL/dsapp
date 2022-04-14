class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self,*args):
        self.size = 0
        if args != ():
                for i in args:
                    self.push(i)

    # For print
    def __str__(self):
        self.to_return = []
        i = self.top
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return str(self.to_return)

    # For other prints
    def __repr__(self):
        self.to_return = []
        i = self.top
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return str(self.to_return)
    
    # For length
    def __len__(self):
        return self.size

    # Add item at the top - return nothing - always O(1)
    def push(self,data):
        if self.size == 0:
            self.top = Node(data)
            self.top.next = None
        elif self.size == 1:
            self.bottom = Node(data)
            self.bottom.next = None
            self.top.next = self.bottom
        else:
            self.new_top = Node(data)
            self.old_top = self.top
            self.new_top.next = self.old_top
            self.top = self.new_top
        self.size += 1
    
    # Delete item at the top - return nothing - always O(1)
    def pop(self):
        if self.size == 0:
           print("It's empty")
        else:
            self.top = self.top.next
        self.size -= 1
        

    # Check item at the top - return data of item at the top - O(1)
    def peek(self):
        if self.top is not None:
            print(self.top.data)
            return self.top.data
        else:
            print("It's empty")


    # Traverse the stack - return stack in list - always O(n)
    def traverse(self):
        self.to_return = []
        i = self.top
        while i is not None:
            self.to_return.append(i.data)
            i = i.next
        return self.to_return

     # Return the size - return number of items in stack - always O(1)
    def return_size(self):
        return self.size

# TESTS

# stack = Stack("Hello","Its","Stack","Implementation")
# stack.peek()
# print(stack.return_size())
# stack.peek()
# print(stack)
# print(stack.traverse())
# stack.pop()
# stack.pop()
# print(stack)
# stack.push("Tests")
# print(stack)
# stack.peek()
# print(stack)
# print(len(stack))
# print(stack.return_size())
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.peek()
# print(stack)
# stack.push("Test")
# print(stack)
