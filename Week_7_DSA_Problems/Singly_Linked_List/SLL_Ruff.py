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
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1


    def get(self, index):
        if index < 0 or index >= self.length:
            return "index out of range"
        curr = self.head
        for i in range (index):
            print(curr.value)
            curr = curr.next
        return curr.value


    def traverse(self):
        if self.head is None:
            return "sll is empty"
        else:
            curr = self.head
            while curr:
                print(curr.value, end="->")
                curr = curr.next
            print(None)


    def get_mid(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return f"The middle node of SLL is: '{slow.value}'"
    

    def cycle_detection(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return "cycle detected"
        return "no cycle detected"
    
            
    # def nth_node_from_end(self, n):
    #     i = self.length-n
    #     return f"{n}th node from last is '{self.get(i)}'"
        
    def kth_from_end(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.value


    def reverse_SLL(self):
        curr = self.head
        self.head = self.tail
        self.tail = curr
        before = None
        after = curr.next
        for _ in range(self.length):
            after = curr.next
            curr.next = before
            before = curr
            curr = after

    # returns set
    def remove_duplicate(self):
        unique = []
        curr = self.head
        while curr:
            if curr.value not in unique:
                unique.append(curr.value)
            curr = curr.next
        return unique
    
    # removes duplicates from linkedlist
    def remove_duplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                if curr.prev:
                    curr.prev = curr.next
                else:
                    self.head = curr.next
            curr = curr.next


    def remove_all_occurances(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                if curr.prev :
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
            curr = curr.next
        

    def sum_SLL_values(self):
        curr = self.head
        total = 0
        while curr:
            total += curr.value
            curr = curr.next
        return f"The sum of values of SLL is: {total}"


    def size_of_sll(self):
        if self.head is None:
            return 0
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count


    # def even_odd_list(self):
    #     if self.head is None:
    #         return []
    #     else:
    #         even = []
    #         odd = []
    #         for i in range (self.length):
    #             if i%2 == 0:
    #                 even.append(self.get(i))
    #             else:
    #                 odd.append(self.get(i))
    #         return even + odd
    
    def even_odd(self):
        if self.head is None:
            return []
        even = []
        odd = []
        curr = self.head
        while curr:
            if curr:
                odd.append(curr.value)
                curr = curr.next.next

            else:
                even.append(curr.value)
        return odd + even

    def merge_sorted_lists(l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


    def delete_value(self, value):
        if self.head is None:
            return "empty"
        if self.head.value == value:
            self.head = None
            
        prev = None
        curr = self.head
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def node_count(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def search_val_get_index(self, value):
        curr = self.head
        count = 0
        while curr:
            if curr.value == value:
                return f"search value{value} found at index {count}"             
            count += 1
            curr = curr.next
        return "search value not found"


    def list_to_SLL(self, list):
        for i in list:
            print(self.append(i))


z = SLL()
z.append(1)
z.append(2)
z.append(3)
z.append(4)
z.append(5)

z.traverse()

# print(z.get_mid())

# z.tail.next=z.head.next
# print(z.cycle_detection())

# print(z.nth_node_from_end(2))

# z.reverse_SLL()

# print(z.remove_duplicate())


# print(z.sum_SLL_values())

# print(z.binary_decimal())

# print(z.size_of_sll()) 

# print(z.kth_from_end(3))

# z.delete_value(3)

# print(z.node_count())

# print(z.search_val_get_index(12))


z.traverse()






