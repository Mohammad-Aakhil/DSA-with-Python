class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None

class singlylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        self.length += 1
        # return True



    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1


    
    def First_pop(self):
        if self.length == 0:
            print("ntg to pop")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1


    def Last_pop(self):
        if self.length == 0:
            print("ntg to pop")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.tail = curr
        self.length -= 1


    def get(self, index):
        if index < 0 or index > self.length:
            print("Check index, it's out of range")
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr

        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            print("value set sucessfully")
        print("None")


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        new_node.next = after
        self.length+=1
        

        
    def delete(self, index):
        if index < 0 and index >= self.length:
            return None
        if index == 0:
            return self.First_pop()
        if index == self.length-1 :
            return self.Last_pop()
        before = self.get(index-1)
        after = before.next
        before.next = after.next
        after = None
        self.length -=1
        return 




    def traverse(self):
        if self.length == 0:
            print("SLL is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end="->")
                curr = curr.next
            print("None")




z = singlylinkedlist()
z.prepend(3)
z.prepend(2)
z.prepend(4)
z.append([4,5,6,7])
# z.Last_pop()
# z.get(3)
# z.set(0, 3)
# z.insert(2,3)
# z.delete(2)
z.traverse()
                
