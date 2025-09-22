class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.end = None
        self.size = 0

    def Enqueue(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.end = new_node
            print(f"Enqueue of {new_node.value} succesful")
        
        else:
            new_node.next = self.top
            self.top = new_node
        print(f"Enqueue of {new_node.value} succesful")

    def Dequeue(self):
        if self.top is None:
            return "Stack is empty"
        else:
            prev = None
            curr = self.top
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            self.end = prev
        print(f"Dequeue of {curr.value} successful")                


    def view_Queue(self):
        if self.top is None:
            return "Queue is empty"
        else:
            print("Enqueue-->", end="")
            curr = self.top
            while curr:
                print(curr.value, end = "-")
                curr = curr.next
            print("->Dequeue")


# q = Queue()
# q.Enqueue(5)
# q.Enqueue(4)
# q.Enqueue(3)
# q.Enqueue(2)
# q.Enqueue(1)
# q.Dequeue()
# q.Dequeue()
# q.view_Queue()



class queue_using_stack:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []


    def Enqueue(self, x):
        self.stack_1.append(x)


    def Dequeue(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        if not self.stack_2:
            return "queue is empty"
        
        return self.stack_2.pop()
    

    def peek(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        if not self.stack_2:
            return "Queue is empty"
        return self.stack_2[-1]
    
    def empty_check(self):
        if not self.stack_1 and not self.stack_2:
            return "Queue is empty"
        else:
            return "Not empty"
        

# q = queue_using_stack()
# q.Enqueue(1)
# q.Enqueue(2)
# q.Enqueue(3)
# print(q.stack_1)
# print(q.stack_2)
# print("peek is ",q.peek())
# print(q.stack_1)
# print(q.stack_2)
# print("dequeue",q.Dequeue())
# print(q.stack_1)
# print(q.stack_2)
# print("peek after dequeue",q.peek())




