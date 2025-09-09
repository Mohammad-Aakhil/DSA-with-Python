class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


    def _hash(self, key):
        return hash(key) % self.capacity
    

    def set_value(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1


    def get_value(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return f"{key} key is not present"
        for k, v in bucket:
            if k == key:
                return v
        return "Match is not present"


    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        if self.table[index] is None:
            return False
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
    
    def keys(self):
        return [k for bucket in self.table if bucket for k, _ in bucket]

    def values(self):
        return [v for bucket in self.table if bucket for _, v in bucket]



h = HashMap(10)
h.set_value("apple", 100)
h.set_value("banana", 200)

print(h.get_value("apple"))     # 100
print(h.get_value("grape"))     # "grape key is not present"

h.set_value("banana", 250)      # Update value
print(h.get_value("banana"))    # 250

h.remove("apple")
print(h.get_value("apple"))     # "apple key is not present"

print(h.keys())                 # ['banana']

print(h.values())               # [250]
