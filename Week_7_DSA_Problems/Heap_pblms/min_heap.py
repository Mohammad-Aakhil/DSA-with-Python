import heapq

class Heap:
    def __init__(self):
        self.heap = []

    
    def insert(self, value):
        heapq.heappush(self.heap, value)

    # def insert_list(list):
    #     heapq.heapify(list)
    #     return [heapq.heappop(list) for _ in range(len(list))]

    def get_min(self):
        return self.heap[0] if self.heap else None


    def pop_min(self):
        heapq.heappop(self.heap) if self.heap else None

    def view_heap(self):
        if self.heap:
            print(self.heap) 
        else :
            None


hp = Heap()
hp.insert(3)
hp.insert(6)
hp.insert(12)
hp.insert(7)
print(hp.heap)

# print(hp.insert_list([4,5,8,2,3]))
print(hp.get_min())
hp.pop_min()
print(hp.heap)
hp.view_heap()

