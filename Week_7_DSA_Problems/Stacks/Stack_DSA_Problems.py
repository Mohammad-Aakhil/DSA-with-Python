class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        # self.max_limit = 99     #optional, if want size restricted stack

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            print(f"Pushed {value} to stack successfully")
        else:
            new_node.next = self.top
            self.top = new_node
            print(f"Pushed {value} to stack successfully")

    def pop(self):
        if self.top is None:
            return "ntg to pop"
        else:
            prev_top = self.top
            self.top =  prev_top.next
            prev_top.next = None
            print(f"popped {prev_top.value} from stack successfully")

    def peek(self):
        if self.top is None:
            return "stack is empty"
        else:
            return f"top is {self.top.value}"
        

    def view_stack(self):
        if self.top is None:
            return "stack is empty"
        else:
            curr = self.top
            print("Stack has :-")
            print("Top->", end="")
            while curr:
                print(curr.value, end="<-")
                curr = curr.next
            print("None")


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.view_stack()
print(s.peek())

s.pop()
s.pop()
s.pop()
s.view_stack()
print(s.peek())
