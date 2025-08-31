class Node:
    def __init__(self, value):
        self.value = value
        self.next =None
        self.prev = None

class DLL:
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
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def first_pop(self):
        if self.head is None:
            print("Ntg to pop")
        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def last_pop(self):
        if self.head is None:
            print("ntg to pop")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1


    def view_DLL(self):
        curr = self.head
        while curr:
            print(curr.value, end="-><-")
            curr = curr.next
        print("None")
        


z = DLL()
z.prepend(9)
z.prepend(8)
z.prepend(7)
# z.first_pop()
# z.first_pop()
# z.first_pop()
z.last_pop()
z.view_DLL()