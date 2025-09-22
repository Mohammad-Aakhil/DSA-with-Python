import heapq

class Heap:
    def __init__(self):
        self.Max_heap = []

    def heap_push(self, value):
        heapq.heappush(self.Max_heap, -value)

    def get_root(self):
        return -self.Max_heap[0] if self.Max_heap else None
    
    def pop_root(self):
        return -heapq.heappop(self.Max_heap) if self.Max_heap else None


    