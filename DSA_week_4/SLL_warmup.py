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
        self.length += 1

    def first_pop(self):
        if self.head is None:
            print("ntg to pop")
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            pop = self.head
            self.head = pop.next
            pop.next = None
        self.length -= 1

    def last_pop(self):
        if self.head is None:
            print("ntg to pop")
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            prev = None
            curr = self.head
            while curr.next :
                prev = curr
                curr = curr.next
            self.tail = prev
            prev.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            # print(f"'{curr.value}' is the value at index: {index}")
            return curr


    def set(self,index, value):
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
        # before = self.get(index-1)
        # after = before.next
        # before.next = new_node
        # new_node.next = after

        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

        self.length +=1

    def delete(self, index):
        if index < 0 or index >= self.length :
            print("index out of range")
        if index == 0:
            return self.first_pop()
        if index == self.length-1:
            return self.last_pop()
        
        else:
            before = self.get(index-1)
            after = before.next
            before.next = after.next
            after = None
            self.length -=1


            
            

    def view(self):
        curr = self.head
        while  curr :
            print(curr.value, end="->")
            curr = curr.next
        print("None")



s = SLL()
# s.prepend(3)
# s.prepend(2)
# s.prepend(1)
# s.first_pop()
# s.first_pop()
# s.first_pop()
s.append(4)
s.append(5)
s.append(6)
# s.last_pop()
# s.last_pop()
# s.last_pop()
# s.insert(1, "x")
# s.insert(3, "x")
# s.get(1)
s.delete(0)
s.view()