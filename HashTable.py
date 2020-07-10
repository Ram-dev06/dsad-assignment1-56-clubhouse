# -*- coding: utf-8 -*-

############ HashTable helper functions
def hashId(key, size):
    """This function itereate the string and get the ASCI code of each character and do the sumation of asci code and 
    than take the modelo with size. it will give the array index where the key and value will be present. """
    return sum([ord(c) for c in key]) % size


############ HashTable
class HashTable:
    """Hash Table holds the key value pair , the initial capacity of the hash map is defined as 100."""

    def __init__(self, capacity=100):
        """ This method initialize the Hash table with capacity 100. size 
        0 , key array as empty and entry as a array of size of capacity."""
        self.capacity = capacity
        self.size = 0
        self._keys = []
        self._entry = [[] for _ in range(capacity)]

    def _find_by_key(self, key, find):
        """Here ke is a key against which against get the value  find is the function which has passed as closer , 
        the defination of find function will be in the get and put methd from where this function will get called."""
        index = hashId(key, self.capacity) # Get the index/ bucket based on hash code of the key
        
        hash_table_cell = self._entry[index]
        found_item = None
        for item in hash_table_cell: #Iterrate the entry array and check the key is matching  and if key is same than get the value
            if item[0] == key:
                found_item = item
                break

        return find(found_item, hash_table_cell)

    def put(self, key, obj):
        """This method get the value against the key """
        

        def find(found_item, hash_table_cell):
            """This function is a closer function which will pass to the find_by_key function to get the value. the purpose of this 
            function is to check if key is already present than replace the value else append the value in same bucket."""
            if found_item:
                found_item[1] = obj
            else:
                hash_table_cell.append([key, obj])
                self.size += 1
                self._keys.append(key)

        self._find_by_key(key, find)
        return self

    def get(self, key, default=None):
        """This method retrive the value based on key.  """
        def find(found_item, _):
            """ This is the closer function which will be passed to find by key function , if key found than return the value 
            otherwise return blanck"""
            if found_item:
                return found_item[1]
            else:
                return default

        return self._find_by_key(key, find)

    def remove(self, key, default=None):
       
        def find(found_item, hash_table_cell):
            """This function delete the key and entr if found and return the removed entry or return the blanck.  """
            if found_item:
                hash_table_cell.remove(found_item)
                self._keys.remove(key)
                self.size -= 1
                return found_item[1]
            else:
                return default

        return self._find_by_key(key, find)
    
    def clear(self):
        self._keys.clear()
        self._entry.clear()
        self.size=0
   
    ####### Python's dict interface

    def keys(self):
        return self._keys

    def values(self):
        res = [] 
        for val in self._entry: 
            if val != [] : 
                res.append(self.get(val[0][0]))
        return res
