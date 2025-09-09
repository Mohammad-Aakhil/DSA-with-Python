class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Enqueue(self, value):     #prepend
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def dequeue(self):           #last_pop
        if self.head is None:
            print("queue is empty")
        else:
            prev = None
            curr = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            self.tail = prev
        self.length -=1


    def view_queue(self):
        curr = self.head
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print("None")
    
    def queue_size(self):
        print(f"the size/length of queue is {self.length}")


queue = Queue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)

queue.dequeue()
queue.dequeue()

queue.view_queue()

queue.queue_size()
