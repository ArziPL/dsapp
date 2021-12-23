class HashTable:
    # Constructor - return nothing - O(n) of initial arguments
    def __init__(self,size):
        self.data = [[None,None]] * size
        self.size = size

    # For print
    def __str__(self):
        return str(self.keys_values())

    # For other prints
    def __repr__(self):
        return str(self.keys_values())

    # Hash function - return index(int) - O(1)
    def hash_func(self,key):
        return (key + int(str(key)[0]) + int(str(key)[-1])) % self.size
    
    # Add bucket with key and value - return that bucket(list of key/value) - 
    # If bucket is not taken O(1)
    # If it's taken then O(10) => O(1) until next index is found
    # If next index is not found then O(n) (linear probing) - O(?)
    # I am not sure of time complexity when there's checking if empty, probing, rearranging, adding new values and mayby
    # a lot of probing. Time complexity pretty bad
    def add(self,key,value):
        hash_key = self.hash_func(key)
        if self.data[hash_key] == [None,None]:
            self.data[hash_key] = [key,value]
            print([key,value])
            return [key,value]
        elif self.data[hash_key] != [None,None]:
            probe = 0
            while self.data[hash_key] != [None,None]:
                probe += 1
                key = key + probe
                hash_key = self.hash_func(key)
                if probe == 10:
                    self.rearrange()
                    self.add(key,value)
                    break
            self.data[hash_key] = [key,value]
            print([key,value])
            return [key,value]

    # Delete bucket at index - return nothing - O(1)
    def delete(self,key):
        hash_key = self.hash_func(key)
        self.data[hash_key] = [None,None]

    # Search if something is at index - return value(any) - O(1)
    def search(self,key):
        hash_key = self.hash_func(key)
        if self.data[hash_key][1] == None:
            return -1
        else:
            return self.data[hash_key][1]

    # Check if value is already in - return True/False - O(n)
    def check_if_exist(self,value):
        values = self.values()
        if value in values:
            return True
        else:
            return False
    
    # Rearrange hash table - return nothing - O(n) (O(2n))
    # Take all key/values in current hash table, clear table, increase size of table by 110%
    # Set all old keys/values with new hashes again in new table
    def rearrange(self):
        keys_values = self.keys_values()
        self.size = round((self.size * 1.1)) 
        self.data = [[None,None]] * self.size
        for bucket in keys_values:
            self.add(bucket[0],bucket[1])

    # Get all keys - return list with all keys(list) - O(n)
    def keys(self):
        all_keys = []
        for bucket in self.data:
            if bucket != [None,None]:
                all_keys.append(bucket[0])
        return all_keys

    # Get all values - return list with all values(list) - O(n)
    def values(self):
        all_values = []
        for bucket in self.data:
            if bucket != [None,None]:
                all_values.append(bucket[1])
        return all_values

    # Get all keys with values - return list with all keys/values(list of key/value) - O(n)
    def keys_values(self):
        keys_values = []
        for bucket in self.data:
            if bucket != [None,None]:
                keys_values.append([bucket[0],bucket[1]])
        return keys_values
    
    # Print sefl - return self - O(?)
    def print_all(self):
        print(self.data)
        return self.data

    # Get size - return size(int) - O(1)
    def self_size(self):
        return self.size

# # TESTS

# ht = HashTable(10)
# ht.add(10,"10")
# ht.add(20,"10")
# ht.add(30,"10")
# ht.add(1,"10")
# ht.add(2,"10")
# ht.add(3,"10")
# print(ht)
# ht.delete(20)
# print(ht)
# print(ht.search(6))
# print(ht.check_if_exist("10"))
# print(ht.check_if_exist("2"))
# print(ht.keys())
# print(ht.values())
# print(ht.keys_values())
# ht.print_all()
# print(ht.self_size())
# ht.add(5215,"10")
# ht.add(63274,"10")
# ht.add(5326,"10")
# ht.add(74373,"10")
# ht.add(5326,"10")
# ht.add(74,"10")
# ht.add(53,"10")
# ht.add(773,"10")
# ht.add(63,"10")
# ht.add(42,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# ht.add(50,"10")
# print(ht.self_size())

