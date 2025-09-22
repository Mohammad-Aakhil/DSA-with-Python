# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# # class SLL:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #         self.length = 0

# #     def append(self, value):
# #         new_node = Node(value)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = new_node

# #         else:
# #             self.tail.next = new_node
# #             self.tail = new_node
# #         self.length += 1

# #     def get(self, index):
# #         if index < 0 or index >= self.length:
# #             return "index out of range"
# #         curr = self.head
# #         for i in range(index):
# #             curr = curr.next
# #         return curr.value
    
# #     def traverse(self):
# #         if self.head is None:
# #             print("SLL is empty")
        
# #         else:
# #             curr = self.head
# #             while curr :
# #                 print(curr.value, end = "->")
# #                 curr = curr.next
# #             print("None")

    
# #     #problem 1
# #     def find_mid(self):
# #         slow = fast = self.head
# #         while fast and fast.next:
# #             slow = slow.next
# #             fast = fast.next
# #         return slow.value

    
# #     #problem 2 cycle detection
# #     def has_cycle(self):
# #         slow = fast = self.head

# #         while fast and fast.next:
# #             slow = slow.next          # move 1 step
# #             fast = fast.next.next     # move 2 steps

# #             if slow == fast:
# #                 return "cycle detected"          # cycle detected
# #         return "no cycle detected"

    
# #     # #problem odd even problem
# #     def arrange_even_odd(self):
# #         if not self.head:
# #             return []
# #         else:
# #             even = []
# #             odd = []
# #             for i in range(self.length):
# #                 if i % 2 != 0:
# #                     odd.append(self.get(i))
# #                 else:
# #                     even.append(self.get(i))

# #             return even + odd
            

# #     def nth_node_from_end(self, n):
# #         i = self.length-n
# #         return self.get(i)
    
# #     def print_list(self, head=None):
# #         if head is None:
# #             head = self.head
# #         curr = head
# #         while curr:
# #             print(curr.value, end=" -> ")
# #             curr = curr.next
# #         print("None")

# #     def reverse_SLL(self):
# #         temp = self.head
# #         self.head = self.tail
# #         self.tail = temp
# #         after = temp.next
# #         before = None
# #         for _ in range(self.length):
# #             after = temp.next
# #             temp.next = before
# #             before = temp
# #             temp = after

# # def merge_sorted_lists(l1, l2):
# #     if not l1:   # if first list empty
# #         return l2
# #     if not l2:   # if second list empty
# #         return l1
    
# #     if l1.value < l2.value:
# #         l1.next = merge_sorted_lists(l1.next, l2)
# #         return l1
# #     else:
# #         l2.next = merge_sorted_lists(l1, l2.next)
# #         return l2











# # z = SLL()
# # z.append("1")
# # z.append("2")
# # z.append("3")
# # z.append("4")
# # z.append("5")
# # z.append("6")
# # z.append("7")
# # z.append("8")
# # # z.tail.next = z.head.next
# # # print(z.mid_val())
# # # print(z.has_cycle())
# # print(z.arrange_even_odd())
# # # z.reverse_SLL()
# # z.traverse()
# # print(z.nth_node_from_end(7))
# # # z.swap_two_nodes(2,5)

# # # def create_linked_list(arr):
# # #     sll = SLL()
# # #     for v in arr:
# # #         sll.append(v)
# # #     return sll.head



# # # # --- Example usage ---
# # # l1 = [1, 3, 5]
# # # l2 = [2, 4, 6]

# # # # Step 1: Convert to linked lists
# # # head1 = create_linked_list(l1)
# # # head2 = create_linked_list(l2)

# # # # Step 2: Merge them
# # # merged_head = merge_sorted_lists(head1, head2)

# # # # Step 3: Print merged linked list
# # # SLL().print_list(merged_head)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0


    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

    def get(self,index):
        if index < 0 or index >= self.lenght:
            return "index out of range"
        else:
            curr = self.head
            for _ in range (index):
                curr = curr.next
            return curr.value

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.lenght:
            return "index out of range"
        if index == 0:
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)
        else:
            before = self.get(index-1)
            before.next = new_node
            new_node.next = before.next
        return self
    

    def traverse(self):
        if self.head is None:
            return "SLL is empty"
        curr = self.head
        while curr:
            print(curr.value, end="->")
            curr = curr.next
        print("None")


    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
				




a = SLL()
a.append(1)
a.append(2)
a.append(3)
print(a.get(2))

a.merge_sorted_lists([1,3,5], [2, 4, 6])

a.traverse()










