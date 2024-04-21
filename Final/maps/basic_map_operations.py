# It seems there was a mistake in calling size as a method, it should be accessed directly as it's a property.

class SimpleHashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size
        self.count = 0

    def _get_hash(self, key):
        hash_key = int(key.split('-')[-1])
        return hash_key % self.size

    def get(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    def put(self, key, value):
        hash_key = self._get_hash(key)
        key_value = [key, value]
        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            self.count += 1
            return None
        else:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    old_value = pair[1]
                    pair[1] = value
                    return old_value
            self.map[hash_key].append(key_value)
            self.count += 1
            return None

    def remove(self, key):
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for i in range(len(self.map[hash_key])):
                if self.map[hash_key][i][0] == key:
                    old_value = self.map[hash_key][i][1]
                    del self.map[hash_key][i]
                    self.count -= 1
                    if len(self.map[hash_key]) == 0:
                        self.map[hash_key] = None
                    return old_value
        return None

    def is_empty(self):
        return self.count == 0

# Create a hash map with 5 slots
hash_map = SimpleHashMap(5)

# Test put method - Adding values
put_result1 = hash_map.put('025-61-0000', 'Person A')
put_result2 = hash_map.put('901-11-0000', 'Person B')
put_result3 = hash_map.put('451-22-0000', 'Person C')

# Test get method - Retrieving values
get_result1 = hash_map.get('025-61-0000')
get_result2 = hash_map.get('901-11-0000')
get_result3 = hash_map.get('451-22-0000')

# Test updating an existing entry
put_update_result = hash_map.put('025-61-0000', 'Person A Updated')

# Test remove method
remove_result1 = hash_map.remove('025-61-0000')
remove_result2 = hash_map.remove('999-99-0000')  # Key that does not exist

# Test size and is_empty methods
size_result = hash_map.count
is_empty_result = hash_map.is_empty()

(put_result1, put_result2, put_result3, 
 get_result1, get_result2, get_result3, 
 put_update_result, remove_result1, remove_result2, 
 size_result, is_empty_result)
