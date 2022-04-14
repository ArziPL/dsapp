class Stack:
        def __init__(self,*args):
            self.stack = []
            if args != ():
                for i in args:
                    self.push(i)

        # For print
        def __str__(self):
            return str(self.stack)

        # For other prints
        def __repr__(self):
            return str(self.stack)
        
        # For length
        def __len__(self):
            return len(self.stack)

        # Add item at the end(top) of list - return added data - always O(1)
        def push(self,data):
            self.stack.append(data)
            return data

        # Delete item at the end(top) of the list - return deleted data - always O(1)
        def pop(self):
            if len(self.stack) != 0:
                temp = self.stack.pop()
                return temp

        # Check item at the end(top) of the list - return data at the end(top) of the list - O(1)
        def peek(self):
            if len(self.stack) != 0:
                temp = self.stack[-1:]
                print(temp[0])
                return temp[0]
            else:
                print("It's empty")
        
        # Traverse the stack - return stack in list - always O(n)
        def traverse(self):
            return self.stack
        
        # Return the size - return number of items in stack - always O(1)
        def size(self):
            return len(self.stack)

        

# TESTS

# stack = Stack("Hello","Its","Stack","Implementation")
# print(stack.size())
# stack.peek()
# stack.push("Push")
# stack.push("Test")
# print(stack)
# stack.peek()
# stack.pop()
# stack.pop()
# print(stack)
# stack.peek()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.peek()
# stack.push("Test")
# stack.peek()
# print(stack.traverse())
# print(stack.size())
