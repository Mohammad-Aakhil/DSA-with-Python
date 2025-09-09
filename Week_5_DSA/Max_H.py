import heapq

class Max_heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def get_max(self):
        return -self.heap[0] if self.heap else None
    
    def pop_max(self):
        return -heapq.heappop(self.heap) if self.heap else None
    
    def view_max_heap(self):
        print("Max_heap :", [-value for value in (self.heap)])



max = Max_heap()
max.insert(3)
max.insert(7)
max.insert(21)
max.insert(1)
max.view_max_heap()
print(f"max value is : {max.get_max()}")
print(f"popped value is :{max.pop_max()}")
max.view_max_heap()
print(f"max value is : {max.get_max()}")
print(f"popped value is :{max.pop_max()}")
max.view_max_heap()






