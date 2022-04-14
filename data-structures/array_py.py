class Array:
    # Constructor - return nothing - O(n) of initial arguments
    # O(n) of initial arguments
    def __init__(self,*args):
        self.size = 0
        self.data = {}
        if args != ():
            for index,item in enumerate(args):
                self.data[index] = item
                self.size += 1

    # For print
    def __str__(self):
        return (str(self.data))

    # For other prints
    def __repr__(self):
        return (str(self.data))

    # Print all index/value - return array(dict) - O(n)
    def print_array(self):
        print(self.data)
        return self.data

    # Return length - O(1)
    def length(self):
        return self.size

    # Get item by index - return that item(any) - O(1)
    def get_item(self, index):
        return self.data[index]

    # Get index of item - return index(int) - worst case O(n) (closer to end the worse)
    def get_index(self, item):
        for i in range(self.size):
            if item == self.data.get(i):
                return i

    # Add at the end - return added item(any) - O(1)
    def push(self, item):
        self.data[self.size] = item
        self.size += 1
        return self.data[self.size - 1]

    # Remove at the end - return deleted item(any) - O(1)
    def pop(self):
        oldLastItem = self.data[self.size-1]
        del self.data[self.size-1]
        self.size -= 1
        return oldLastItem

    # Add at the beginning - return added item(any) - always O(n)
    def unshift(self,item):
        for i in range(self.size-1,-1,-1):
            self.data[i+1] = self.data[i] 
        self.data[0] = item
        self.size += 1
        return self.data[0]

    # Remove at the beginning - return deleted item(any) - always O(n)
    def shift(self):
        deleted = self.data[0]
        for i in range(1,self.size):
            self.data[i-1] = self.data[i]
        del self.data[self.size-1]
        self.size -= 1
        return deleted

    # Add at given index - return added item(any) - worst case O(n) (the closer to the beginning the worse)
    def add_at_index(self,index,item):
        for i in range(self.size,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        self.size += 1
        return item

    # Delete at given index - returnd deleted item(any) - worst case O(n) (the closer to the beginning the worse)
    def delete_at_index(self, index):
        deleted = self.data[index]
        for i in range(index, self.size-1):
            self.data[i] = self.data[i+1]
        self.size -= 1
        del self.data[self.size]
        return deleted

    # Reverse order of items - return array(dict) - O(n)
    def reverse(self):
        newDict = {}
        for i in range(self.size):
            newDict[i] = self.data[self.size-i-1]
        self.data = newDict
        return self.data

    # Clear whole array - return empty array(dict) - O(1)
    def clear(self):
        self.size = 0
        self.data = {}
        return self.data


# TESTS

# test = Array("Hello","World")
# print(test)

# test.push("It's")
# test.print_array()
# test.push("Hello")
# test.push("World")
# test.print_array()


# # Adding sample data
# test.push("Hello")
# test.push("World")
# test.push("It's")
# test.push("Array")
# test.push("Implementation")


# # Print + length (all items + length)
# print("PRINT ARRAY + LENGTH ARRAY")
# test.print_array()
# print(test.length())
# print("PRINT ARRAY + LENGTH ARRAY \n")


# # Get item + get index
# print("GET ITEM + GET INDEX")
# print(test.get_item(2))
# print(test.get_index("Array"))
# print("GET ITEM + GET INDEX\n")


# # Push(add at the end)
# print("PUSH TEST")
# print(test.push("PushTest"))
# test.print_array()
# print(test.length())
# print("PUSH TEST \n")


# # Pop(delete at the end)
# print("POP TEST")
# print(test.pop())
# test.print_array()
# print(test.length())
# print("POP TEST \n")


# # Unshift(add at the beginning)
# print("UNSHIFT TEST")
# print(test.unshift("UnshiftTest"))
# test.print_array()
# print(test.length())
# print("UNSHIFT TEST \n")


# # Shift(remove at the beginning)
# print("SHIFT TEST")
# print(test.shift())
# test.print_array()
# print(test.length())
# print("SHIFT TEST \n")


# # Add at index
# print("ADD AT INDEX TEST")
# print(test.add_at_index(2, "add_at_index"))
# test.print_array()
# print(test.length())
# print("ADD AT INDEX TEST \n")


# # Delete at index
# print("DELETE AT INDEX TEST")
# print(test.delete_at_index(2))
# test.print_array()
# print(test.length())
# print("DELETE AT INDEX TEST \n")


# # Reverse order
# print("REVERSE TEST")
# print(test.reverse())
# print(test.length())
# print("REVERSE TEST \n")


# # Clear array/size
# print("CLEAR TEST")
# print(test.clear())
# test.print_array()
# print(test.length())
# print("CLEAR TEST \n")
