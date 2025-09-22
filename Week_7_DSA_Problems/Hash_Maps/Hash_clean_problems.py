class Hash_map:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = [key, value] #updating value if duplicate key is given
                return
        self.table[index].append([key, value])

    def delete(self, key):
        index = self.hash(key)

        if self.table[index] is not None:
            for i,(k,v) in enumerate(self.table[index]):
                if k == key:

                    # self.table[index][i].remove([k,v])
                    self.table[index][i] = None
        # for i,(k,v) in enumerate(self.table[index]):
        #     if k == key:
        #         # del self.table[index][i]
        #         self.table[index][i] = None
        #         return
        else:
            print("no matching key found")
        
    def get_val_by_key(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k == key:
                return v
            else:
                return "key not found"
            
    def get_keys(self):
        all_keys = []

        for buckets in self.table:
            while buckets is None:
                continue
            for k,v in buckets:
                all_keys.append(v)
        return all_keys

    def view_hash_table(self):
            for i in range(10):
                print(f"Hash {i}:- {self.table[i]}")

    

h = Hash_map()
h.insert("train", 25)
h.insert("bus", 20)
h.insert("bruce", 11)
h.insert("bmw", 15)
h.insert("brute", 15)
h.insert("vikings", 15)
h.insert("choking", 15)
h.insert("wresling", 15)
h.insert("striking", 15)
h.insert("mma", 15)
h.insert("ufc", 15)
h.insert("muaithai", 15)
h.insert("buus", 20)
print(h.table)
h.view_hash_table()
h.delete("brute")
h.view_hash_table()

