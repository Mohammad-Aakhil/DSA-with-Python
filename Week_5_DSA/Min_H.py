# import heapq


# class Min_heap:
#     def __init__(self):
#         self.heap = []

#     def insert(self, value):
#         heapq.heappush(self.heap, value)

#     def get_min(self):
#         return self.heap[0] if self.heap else None
    
#     def extract_min(self):
#         return heapq.heappop(self.heap) if self.heap else None
    
#     def display(self):
#         ("Min_Heap :" ,self.heap)



# min = Min_heap()
# min.insert(3)
# min.insert(9)
# min.insert(12)
# min.insert(15)
# min.get_min()
# min.display()
# min.extract_min()
# min.display()


# import heapq

# class Min_heap:
#     def __init__(self):
#         self.heap = []

#     def insert(self, value):
#         heapq.heappush(self.heap, value)

#     def get_min(self):
#         return self.heap[0] if self.heap else None
    
#     def pop_root(self):
#         return heapq.heappop(self.heap) if self.heap else None
    
#     def view_heap(self):
#         print("Min_heap :", self.heap)



# mh = Min_heap()
# mh.insert(3)
# mh.insert(21)
# mh.insert(1)
# (mh.view_heap())
# (mh.pop_root())
# print(mh.get_min())
# (mh.view_heap())


import heapq

class Min_Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def get_root(self):
        return self.heap[0] if self.heap else None
    
    def pop_root(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def view_heap(self):
        print("MIN_Heap :", self.heap)


s = Min_Heap()
s.insert(4)
s.insert(7)
s.insert(6)
s.insert(15)
s.view_heap()

print(s.get_root())
print(s.pop_root())
s.view_heap()