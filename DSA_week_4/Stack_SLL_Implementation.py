class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.max_size = 10

    def length(self):
        print(f"the stack length/size is '{self.size}'" )
        return self.size

    def push(self, value):
        if self.size == self.max_size:
            raise Exception("stack reached max size")
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"'|{self.top.value}|' is pushed to stack", "\n")
        return self.top.value

    def pop(self):
        if not self.size:
            raise Exception("stack is empty")
        prev_top = self.top
        self.top = prev_top.next
        prev_top.next = None
        self.size -=1
        print(f"popped element is '{prev_top.value}' ", "\n")
        return prev_top.value

    def peek(self):
        print(f" '{self.top.value}' is the at peek/top ", "\n")
        return self.top.value if self.top else None
    
    def clear(self):
        self.top = None
        self.size = 0
        print("stack is cleared")
        return self

    def view_stack(self):
        top = self.top
        print("Stack has:")
        while top is not None:
            print( top.value, end ="<-", )
            top = top.next
        print("None", "\n")

s = Stack()
(s.push("first"))
(s.push("second"))
(s.push("third"))
(s.push("fourth"))

s.pop()

# s.clear()


s.view_stack()
s.peek()
s.length()
        