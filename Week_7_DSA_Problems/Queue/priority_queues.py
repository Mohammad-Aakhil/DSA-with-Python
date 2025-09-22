import heapq

# In heapq, by default it's min-heap, so we use negative priorities for max behavior
pq = []

# push elements (priority, value)
heapq.heappush(pq, (-1, "Patient A"))
heapq.heappush(pq, (-5, "Patient B"))
heapq.heappush(pq, (-2, "Patient C"))

# pop elements in order of priority
while pq:
    priority, patient = heapq.heappop(pq)
    print(patient)



import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        # Python heapq is a min-heap → so use negative priority for max-heap behavior
        heapq.heappush(self.queue, (-priority, item))
    
    def dequeue(self):
        if not self.queue:
            return None
        priority, item = heapq.heappop(self.queue)
        return ( -priority, item )  # return priority as positive
    
    def peek(self):
        if not self.queue:
            return None
        priority, item = self.queue[0]
        return (-priority, item)
    
    def is_empty(self):
        return len(self.queue) == 0
