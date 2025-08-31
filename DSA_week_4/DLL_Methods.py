# class Node:
#     def __init__(self, val):
#         self.prev = None
#         self.val = val
#         self.next = None
        

# class Doubly_Linked_List:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def prepend(self, val):
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length +=1 
        


#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
        
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node


#     def L_pop(self):
#         if self.head is None:
#             print("ntg to pop")
#         else:
#             curr = self.head
#             self.head = curr.next
#             curr.next = None


#     def R_pop(self):
#         if self.head is None:
#             print("Ntg to pop")
#         else:
#             last = self.tail
#             self.tail = last.prev
#             last.prev.next = None

        
#         #     curr = self.head
#         #     self.head.next = self.head
#         #     curr.next = None
#         #     self.head.prev = None
#         # return curr.val
        


#     def traverse(self):
#         if self.head is None:
#             print("DLL is empty")
        
#         else:
#             curr = self.head
#             while curr is not None:
#                 print(curr.val, end="-><-")
#                 curr = curr.next
#             print("None")


# d = Doubly_Linked_List()
# d.append(10)
# d.prepend(5)
# d.prepend(3)
# d.L_pop()
# d.L_pop()
# d.L_pop()
# # d.R_pop()
# # d.R_pop()
# d.traverse()




class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None



class doublylinkedlist:
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
        self.length+=1

        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1


    def first_pop(self):
        if self.head is None:
            print("ntg to pop")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1


    def last_pop(self):
        if self.head is None:
            print("ntg to pop")
        elif self.head == self.tail:
            self.head =None
            self.tail =None
        else :
            self.tail = self.tail.prev
            self.tail.next = None 
        self.length -=1


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        curr = self.head
        if index < self.length/2:
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length-1, index, -1):
                curr = curr.prev
        return curr
    
    # def get (self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #         # print("index out of range")

    #     temp = self.head                    #if index is 0
    #     if index < self.length/2:           #traverse only 1st half of the DLL
    #         for _ in range(index):
    #             temp = temp.next
    #     else:
    #         temp = self.tail                #traverse from reverse using tail as starting node
    #         for _ in range(self.length-1, index, -1):
    #             temp = temp.prev

    #     return temp.val                     #without entering if and else loop it returns 1st node


    def set(self, index, value):
        curr = self.get(index)
        while curr:
            curr.val = value
            return True
        return False



    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
            # print("index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.prepend(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length +=1
        return True


    def delete(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.first_pop()
        if index == self.length-1:
            return self.last_pop()

        del_val =self.get(index)

        del_val.next.prev = del_val.prev
        del_val.prev.next = del_val.next
        del_val.prev = None
        del_val.next = None


        # before = self.get(index-1)
        # after = before.next
        # after.prev = before
        # before.next = after

        self.length -= 1
        return del_val.val



    def traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end="-><-")
                curr = curr.next
            print("None")



z = doublylinkedlist()
# z.append(3)
# z.append(4)
# z.append(5)

z.prepend(6)
z.prepend(5)
z.prepend(4)
z.prepend(3)
z.prepend(2)

# z.first_pop()
# z.first_pop()
# z.first_pop()

# z.last_pop()
# z.last_pop()
# z.last_pop()

# print(z.get(2))

# z.insert(-1,"x")

# z.set(0, "x")

print(z.delete(2))
z.traverse()


