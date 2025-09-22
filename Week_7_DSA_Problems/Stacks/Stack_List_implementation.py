class Stack:
    def __init__(self):
        self.main_stack = []

    def push_item(self,x):
        self.main_stack.append(x)

    def push_items(self, list):
        for i in list:
            self.main_stack.append(i)
        
    def stack_pop(self):
        self.main_stack.pop()
        # return f"popped {self.main_stack.pop()}"
    
    def sort_stack(self):
        return sorted(self.main_stack)
    

a = Stack()
a.push_items([5,4,3,2,1])
print(a.main_stack)
print(a.stack_pop())
print(a.sort_stack())
print(a.stack_pop())

    


# class Undo_Redo:
#     def __init__(self):
#         self.undo_stack = []
#         self.redo_stack = []

#     def do(self, action):
#         self.undo_stack.append(action)
#         self.redo_stack.clear()


#     def undo(self):
#         if not self.undo_stack:
#             return "ntg to undo"
#         action = self.undo_stack.pop()
#         self.redo_stack.append(action)
#         return action


#     def redo(self):
#         if not self.redo_stack:
#             return "ntg to redo"
#         action = self.redo_stack.pop()
#         self.undo_stack.append(action)
#         return action


# u = Undo_Redo()
# u.do(1)
# u.do(2)
# u.do(3)
# u.do(4)
# u.do(5)
# u.undo()
# u.undo()
# u.undo()
# u.redo()
# u.redo()
# u.redo()
# print(u.undo_stack)
# print(u.redo_stack)


# def is_balanced(s):
#     stack = []
#     pairs = {']':'[', '}':'{', ')':'('}

#     for char in s:
#         if char in '[{(':
#             stack.append(char)
        
#         elif char in ']})':
#             if not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()
#     return not stack

# # print(is_balanced('[{()}]'))

# def is_balanced(s):
#     stack = []
#     pairs = {')':'(', '}':'{', ')':'('}

#     for char in s:
#         if char in '{([':
#             stack.append(char)
#         elif char in '])}':
#             if not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()
#     return not stack
        
# def is_balanced(s):
#     stack = []
#     pairs = {']':'[', '}':'{', ')':'('}
#     for char in s:
#         if char in '[{(':
#             stack.append()
#         # elif:
#         if char in ']})':
#             if not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()
#     return not stack

# class undo_redo:
#     def __init__(self):
#         self.undo_stack = []
#         self.redo_stack = []


#     def add(self, page):
#         self.undo_stack.append(page)
#         self.redo_stack.clear()

#     def undo(self):
#         if not self.undo_stack:
#             return "ntg to undo"
#         page = self.undo_stack.pop()
#         self.redo_stack.append(page)
#         return f"curr page after undo is {self.undo_stack[-1]}"
    
#     def redo(self):
#         if not self.redo_stack:
#             return "ntg to redo"
#         page = self.redo_stack.pop()
#         self.undo_stack.append(page)
#         return f"curr page after undo is {self.undo_stack[-1]}"


# a = undo_redo()
# a.add("google")
# a.add("leetcode")
# a.add("lenskart")
# print(a.undo_stack)
# print(a.redo_stack)
    

# print(a.undo())
# print(a.undo_stack)
# print(a.redo_stack)
# print(a.undo())
# print(a.undo_stack)
# print(a.redo_stack)
# print(a.redo())
# print(a.undo_stack)
# print(a.redo_stack)



# def binary_string_generation(n, current = ""):
#     if len(current) == n:
#         print(current)
#         return 
    
#     binary_string_generation(n, current + "0")
    
#     binary_string_generation(n, current + "1") 
    
# binary_string_generation(2)

# class stack:
#     def __init__(self):
#         self.to_sort = []

#     def add_stack(self, stack):
#         for i in stack:
#             self.to_sort.append(i)

#     def sort_stack(self):
#         return sorted(self.to_sort)
            
#     def min_val(self):
#         return self.sort_stack()[0]
    
#     def next_greater_element(self):
#         return self.sort_stack()[ (len(self.sort_stack())) - 2]
    
# s = stack()
# s.add_stack([5,2,4,7,3,6,1])
# print(s.sort_stack())
# print(s.min_val())
# print(s.next_greater_element())


string_1 = "car.train.bus.chopper"
list_str = string_1.split(".")
print(string_1)
print(list_str)
print(type(string_1))
print(type(list_str))
