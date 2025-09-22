class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def prepend(self, value):
        new_node = Node(value)
        if self.head == self.tail == None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def pop_right(self):
        if self.head and self.tail is None:
            return "SLL is  empty"
        else:
            curr = self.head
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next
            self.tail = prev
            prev.next = None
        self.length -= 1


    def pop_left(self):
        if self.head is None:
            return "sll id empty"
        else:
            self.head = self.head.next
        self.length -= 1


    def get(self, index):
        if index < 0 or index >= self.length:
            return "index out of range"
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr
        
    def set(self, index, value):
        if self.head is None:
            return "sll is empty"
        set_val = self.get(index)
        while set_val:
            set_val.value = value
            print("update successful")
            return True
        return False
        
            
    def remove(self, index):
        if index < 0 or index >= self.length:
            return "index out of range"
        if index == 0:
            return self.pop_left()
        if index == self.length-1:
            return self.pop_right()
        else:
            before = self.get(index-1)
            del_node = before.next
            after = del_node.next
            before.next = after
        self.length -= 1


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return "index out of range"
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next
            before.next = new_node
            new_node.next = after
        self.length +=1


    def reverse_list(self):
        curr = self.head
        before = None
        after = curr.next
        while curr:
            after = curr.next
            curr.next = before
            before = curr 
            curr = after
        self.head = self.tail
        self.tail = curr


    def is_cycle(self):
        # if self.head is None:
        #     return "sll is empty"
        # else:
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    print("cycle detected")
                    return True
                print("no cycle deected")
                return False


    def mid_val(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle Node value is:- {slow.value}")


    def merge_sorted_lists(self, l1, l2):
        merged_list = sorted(l1+l2)
        for i in merged_list:
            self.append(i)


    def merge_unsorted_list(self,l1,l2):
        s_l1 = sorted(l1)
        s_l2 = sorted(l2)
        merged_list = sorted(s_l1+s_l2)
        for i in merged_list:
            self.append(i)

        self.length += len(l1+l2)


    def delete_nth_from_end(self, n):
        del_idx = self.length-n
        self.remove(del_idx)


    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value, end = "->")
            curr = curr.next
        print("None")


sll = SLL()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
# sll.tail.next = sll.head.next.next
# sll.traverse()
# sll.pop_right()
# sll.pop_left()

# print(sll.get(-3))

# sll.remove(2)
# sll.set(2,33)
sll.insert(0,0)
sll.insert(6,6)
sll.insert(4,44)
# sll.reverse_list()
# sll.is_cycle()
sll.traverse()

m = SLL()
m.merge_sorted_lists([1,7,3,4,2],[8,5,9,6])
m.traverse()

n = SLL()
n.merge_unsorted_list([1,7,3,4,2],[8,5,9,6])
n.traverse()
print(m.length)


sll.delete_nth_from_end(4)
sll.traverse()

# print(sll.length)


    