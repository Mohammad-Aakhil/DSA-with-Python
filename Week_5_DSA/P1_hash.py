# class hash1:
#     def __init__(self,capacity=10):
#         self.capacity=capacity
#         self.size=0
#         self.table=[None] * capacity


#     def hash(self,keys):
#         return hash(keys) % self.capacity


#     def set_value(self,key,value):
#         index=self.hash(key)
#         if self.table[index] == None:
#             self.table[index]=[]
#         for i,k in enumerate(self.table[index]):
#             if k==key:
#                 self.table[index][i] = (key,value)
#         self.table[index].append((key,value))
#         self.size+=1


#     def get_values(self,keys):
#         index=self.hash(keys)
#         if self.table[index] is None:
#             return f"{keys} key is not present"
#         for k,v in self.table[index]:
#             if k == keys:
#                 return v
#         else:
#             return "Match is not not present"
        

#     def keys(self):
#         all_keys=[]
#         for bucket in self.table:
#             if bucket is None:
#                 continue
#             for k,_ in bucket:
#                 all_keys.append(k)
#         return all_keys


#     def values(self):
#         all_values=[]
#         for bucket in self.table:
#             if bucket is None:
#                 continue
#             for _,v in bucket:
#                 all_values.append(v)
#         return all_values


# l=hash1(10)
# l.set_value("pavan",100)
# l.set_value("aakhil",200)
# print(l.get_values("pavan"))
# print(l.get_values("dp"))
# print(l.keys())
# print(l.values())
# print(l.table)

# class Hash_map:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.table = [None] * capacity

#     def hash(self, key):
#         return hash(key) % self.capacity
    
#     def insert(self, key, value):
#         index = self.hash(key)

#         if self.table[index] == None:
#             self.table[index] = []

#         for i, (k,v) in enumerate (self.table[index]):
#             if k == key:
#                 self.table[index][i] = [(key, value)]

#         self.table[index].append([key, value])


#     def get_val_by_key(self, key):
#         index = self.hash(key)
#         bucket = self.table[index]

#         if bucket is not None:

#             for k,v in bucket:
#                 return v
#         else:
#             return f"key '{key}' not present" 

    

#     def all_keys(self):
#         all_keys = []

#         for buckets in self.table:
#             if buckets is None:
#                 continue
#             for k,_ in buckets:
#                 all_keys.append(k)
#             return all_keys




# a = Hash_map(10)
# a.insert("johnbones", 29)
# print(a.table)
# print(a.hash("johnbones"))
# print(a.get_val_by_key("johnjones"))
# print(a.get_val_by_key("johnbones"))
# print(a.all_keys())


# class Hash_map:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.table = [None] * capacity


#     def hash(self, key):
#         return hash(key) % self.capacity


#     def insert_pair(self, key, value):
#         index = self.hash(key)

#         if self.table[index] is None:
#             self.table[index] = []

#         for i, (k,v) in enumerate (self.table[index]):
#             if k == key:
#                 self.table[index][i] == [key, value]
#                 return
            
#         self.table[index].append([key, value])


# a = Hash_map(10)
# a.insert_pair("donbones", 29)
# print(a.table)
# print(a.hash("donbones"))   


class Hash_map:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity


    def K_hash(self, key):
        return hash(key) % self.capacity


    def Insert_pair(self, key, value):
        index = self.K_hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for i, (k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i] = [key, value]

        self.table[index].append((key, value))
        

    def delete_pair(self, key):
        index = self.K_hash(key)

        if self.table[index]:
            for i, (k,v) in enumerate(self.table[index]):
                if k==key:
                    self.table.pop(index) 
        else:
            return "ntg to delete"
            
    
    def get_value(self, key):
        index = self.K_hash(key)
        bucket = self.table[index]

        if bucket :
            for k,v in bucket:
                if k==key:
                    return v
                else:
                    return "empty bucket"                
        return "key does'nt exist"


    def all_keys(self):
        all_keys=[]

        for keys in self.table:
            if keys is None:
                continue
            for k,_ in keys:
                all_keys.append(k)
        return all_keys
    

    def all_values(self):
        all_values = []
        for values in self.table:
            if values is None:
                continue
            for _,v in values:
                all_values.append(v)
        return all_values
    


a = Hash_map(10)
a.Insert_pair("MI", 5)
a.Insert_pair("csk", 6)
a.Insert_pair("dc", 1)
print(a.table)

            
print(a.get_value("mi"))

print(a.all_keys())
print(a.all_values())

a.delete_pair("dc")
print(a.table)

a.Insert_pair("dc", 1)
print(a.table)
