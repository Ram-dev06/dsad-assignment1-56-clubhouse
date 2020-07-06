# -*- coding: utf-8 -*-

############ HashTable helper functions
def hashId(key, size):
    return sum([ord(c) for c in key]) % size


############ HashTable
class HashTable:
   

    def __init__(self, capacity=1000):
        """ Capacity defaults to 1000. """

        self.capacity = capacity
        self.size = 0
        self._keys = []
       
        self._values = [[] for _ in range(capacity)]

    def _find_by_key(self, key, find):
        index = hashId(key, self.capacity)
        
        hash_table_cell = self._values[index]
        found_item = None
        for item in hash_table_cell:
            if item[0] == key:
                found_item = item
                break

        return find(found_item, hash_table_cell)

    def put(self, key, obj):
        

        def find_result_func(found_item, hash_table_cell):
            if found_item:
                found_item[1] = obj
            else:
                hash_table_cell.append([key, obj])
                self.size += 1
                self._keys.append(key)

        self._find_by_key(key, find_result_func)
        return self

    def get(self, key):
       
        def find_result_func(found_item, _):
            if found_item:
                return found_item[1]
            else:
                return ''

        return self._find_by_key(key, find_result_func)

    def remove(self, key):
       
        def find_result_func(found_item, hash_table_cell):
            if found_item:
                hash_table_cell.remove(found_item)
                self._keys.remove(key)
                self.size -= 1
                return found_item[1]
            else:
                return ""

        return self._find_by_key(key, find_result_func)


    ####### Python's dict interface


    def keys(self):
        return self._keys

    def values(self):
        res = [] 
        for val in self._values: 
            if val != [] : 
                res.append(self.get(val[0][0]))
        
        return res

  

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

if __name__ == "__main__":
    # Run unit tests
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*hashtable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)