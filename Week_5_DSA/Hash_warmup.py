# class Hash_map:
#     def __init__(self, capacity = 10):
#         self.capacity = capacity
#         self.size = 0
#         self.table = [None] * capacity

#     def hash(self, key):
#         return hash(key) % self.capacity
    

#     def set(self, key, value):
#         index = self.hash(key)
#         if self.table[index] is None:
#             self.table[index] = []

#         for i,(k,v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index][i] = (key, value)
#                 return

#         self.table[index].append((key, value))


#     # def get(self, key):
#     #     index = self.hash(key)
#     #     bucket = self.table[index]

#     #     if bucket is None:
#     #         return "bucket is empty"
        
#     #     for k,v in bucket:
#     #         if k == key:
#     #             return v
            
#     #     return "key not found"



#     def get(self, key):
#         index = self.hash(key)
#         bucket = self.table[index]

#         if bucket is None:
#             print("empty")

#         for k,v in bucket :
#             k == key
#             return v
#         return "key not found"


# # x = Hash_map()
# # x.set("Khabib", 29)
# # x.set("magomed", 23)
# # x.set("tyson", 48)
# # x.set("khamzat", 15)
# # print(x.get("Khabib"))
# # print(x.get("tyson"))
# # print(x.get("magomed"))
# # print(x.table)



# class Hash_map:
#     def __init__(self, capacity = 10):
#         self.capacity = capacity
#         self.size = 0
#         self.table = [None] * capacity


#     def hash(self, key):
#         return hash(key) % self.capacity
    
    
#     def set(self, key, value):
#         index = self.hash(key)

#         if self.table[index] is None:
#             self.table[index] = []
        
#         for i, (k,v) in enumerate(self.table[index]):
#             if k == key:
#                 self.table[index][i] == (key, value)
#                 return
            
#         self.table[index].append((key, value))
#         self.size += 1


#     def get(self, key):
#         index = self.hash(key)
#         bucket = self.table[index]

#         if self.table[index] is None:
#             return "key not found"
        
#         for k,v in bucket:
#             if k == key:
#                 return v
#         return "empty"
    

#     def remove(self, key):
#         index = self.hash(key)
#         bucket = self.table[index]

#         if self.table[index] is None:
#             return "bucket is empty"
        
#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 bucket.pop(i)
#                 self.size -= 1
#                 return True
#         return False
            

# z = Hash_map()
# z.set("apple", 12)
# z.get("apple")
# print(z.table)
# print("before remove")
# print(z.remove("apple"))
# print(z.table)


# def find_common(x,y):
#     for i in x:
#         for j in y:
#             if i == j:
#                 return (j)
# print(find_common([1,2,3,4,5], [4,5,6,7]))         



class Hash_map:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self,  key, value):
        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for i, (k,v) in enumerate (self.table[index]):
            if k == key:
                self.table[index][i] = [key, value]
                return

        self.table[index].append([key, value])


    def get_val(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        if bucket is None:
            return "no key found"
        for _,v in bucket:
            return v
            
        return "key not found"
    
    
    def keys(self):
        all_keys = []

        for bucket in self.table:
            if bucket is None:
                continue
            for k,_ in bucket:
                all_keys.append(k)
        return all_keys
        

    def all_values(self):
        all_vals = []

        for bucket in self.table:
            if bucket is None:
                continue
            for _,v in bucket:
                all_vals.append(v)
            
        return all_vals



z = Hash_map(10)
z.insert("kebab", 450)
z.insert("habib", 333)
print(z.get_val("zabit"))
print(z.get_val("kebab"))
print(z.keys())
print(z.all_values())
print(z.table)





