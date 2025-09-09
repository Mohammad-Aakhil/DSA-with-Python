class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None        
        self.tail = None        
        self.length = 0



    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1



    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1



    def first_pop(self):
        if self.head is None:
            print("NTG TO POP")

        if self.head.next is None:
            self.head = None
            self.tail = None

        else:
            curr = self.head
            self.head = curr.next
            curr = None
        self.length -=1




    def last_pop(self):
        if self.head is None:
            print("ntg to pop")

        if self.head.next is None:
            self.head = None
            self.tail = None

        else:
            prev = None
            curr = self.head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            self.tail = prev
            self.tail.next = None    
        self.length -=1
        


    def get (self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr



    # def get (self, index):
    #     if index < 0 or index >= self.length:
    #         print("index out of range")
    #     curr = self.head
    #     for _ in range(index):
    #         curr = curr.next
    #     print(f"'{curr.value}' is the value at index: {index}")
    


    def set(self, index, value):
        curr = self.get(index)
        if curr:
            curr.value = value
            return True
        return False


    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("index out of range")

        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        before.next = new_node
        new_node.next = after

        self.length +=1


    def delete(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None

        if index == 0:
            return self.first_pop()
        
        if index == self.length-1:
            return self.last_pop()
        
        before = self.get(index-1)
        after = before.next
        before.next = after
        after.next = None

        self.length -=1



    def traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end="->")
                curr = curr.next
            print("None")



a = SLL()
# a.prepend(54)
# a.prepend(43)
# a.prepend(32)
# a.prepend(21)

a.append(65)
a.append(76)
a.append(87)
a.append(98)

# a.first_pop()
# a.first_pop()
# a.first_pop()

# a.last_pop()
# a.last_pop()
# a.last_pop()

# print(a.get(3))

# a.set(1, 33)

a.insert(1,'dc')
a.insert(5,'woo')
a.insert(0,'ufc')

a.delete(6)

a.traverse()


