class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


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


    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_by_index(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return "index out of bound"
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            prev = None
            curr = self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            prev.next = new_node
            new_node.prev = prev
            new_node.next = curr
            curr.prev = new_node   


    def delete_head(self):
        if self.head is None:
            return "dll is empty"
        else:
            curr = self.head 
            new_head = curr.next
            self.head = new_head
            curr.next = None
            del curr

    def delete_tail(self):
        if self.head is None:
            return "dll is empty"
        else:
            curr = self.tail
            new_tail = curr.prev
            new_tail.next = None
            curr.prev = None
            self.tail = new_tail


    def delete_by_val(self, value):
        if self.head is None:
            return "dll is empty"
        if self.head.value == value:
            self.head = None
        else:
            prev = self.head
            curr = prev.next
            while curr:
                if curr.value == value:
                    prev.next = curr.next.prev
                    curr.next.prev = prev
                    curr.next = None
                    curr.prev = None
                prev = curr
                curr = curr.next


    def palindrome(self):
        left = self.head
        right = self.tail
        while left and right and left != right and left.prev != right:
            if left.value != right.value:
                return "given DLL is not a palindrome"
            left = left.next
            right = right.prev
        return "given DLL is a palindrome"


    def remove_all_occurances(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
            curr = curr.next
                # if curr.next:
                #     curr.next.prev = curr.prev
                # else:
                #     self.tail = curr.prev


    def remove_duplicate_by_value(self, value):
        curr = self.head
        found = False

        while curr:
            if curr.value == value:
                if not found:
                    # First occurrence → keep it
                    found = True
                    curr = curr.next
                else:
                    # Duplicate occurrence → remove it
                    nxt = curr.next
                    if curr.prev:
                        curr.prev.next = nxt
                    if nxt:
                        nxt.prev = curr.prev
                    # If tail is being removed, update tail
                    if curr == self.tail:
                        self.tail = curr.prev
                    curr = nxt
            else:            
                curr = curr.next
                


    def remove_duplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        # #tracking tail pointer to remove duplicates

        # curr = self.tail
        # while curr and curr.prev:
        #     if curr.value == curr.prev.value:
        #             curr.prev = curr.prev.prev
        #     else:
        #         curr = curr.prev



    def traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            curr = self.head
            while curr:
                print(curr.value, end="-><-")
                curr = curr.next
            print("None")


    def reverse_traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            curr = self.tail
            while curr:
                print(curr.value, end="-><-")
                curr = curr.prev
            print("None")


    def reverse_DLL(self):
        if self.head and self.head.next is None:
            return "can't reverse a empty or single node"
        curr =  self.head
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        self.head, self.tail = self.tail, self.head

    # def 

    def mid_val(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        return slow.value


    def cycle_detection(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "cycle deteted"
        return "no cycle detected"


d = DLL()
d.append(1)
d.append(1)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(5)
d.append(5)
d.append(5)
d.append(5)
d.append(6)
d.append(7)
d.append(7)
d.append(7)
d.traverse()

# d.insert_by_index(1,"x")

# d.delete_head()
# d.delete_head()

# d.delete_tail()

# d.delete_by_val(2)

# d.tail.next =d.head.next
# print(d.cycle_detection())
# d._traverse()
# print(d.mid_val())
# print(d.palindrome())

d.remove_duplicates()
# d.remove_all_occurances(1)
# d.remove_all_occurances(5)
# d.remove_all_occurances(7)

# d.remove_duplicate_by_value(5)

d.traverse()
# d._traverse()




