# Singly Linked List (SLL)

# 1.Reverse a linked list (iterative + recursive)

# 2.Detect cycle in a linked list (Floyd’s Cycle Detection)

# 3.Find the middle of a linked list (fast & slow pointers)

# 4.Merge two sorted linked lists

# 5.Remove nth node from the end

# 6.Palindrome linked list check

# 7.Intersection point of two linked lists

# 8.Add two numbers represented by linked lists

# 9.Rotate linked list by k positions

# 10.Sort a linked list (Merge Sort on linked list)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


    def find_middle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value


    def merge_lists(l1, l2):
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


    def remove_nth_from_end(head, n):
        dummy = Node(0)
        dummy.next = head
        first = second = dummy
        for _ in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


    def is_palindrome(head):
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Compare two halves
        left, right = head, prev
        while right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next
        return True


    def get_intersection_node(headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a  # either intersection node or None
    

    def add_two_numbers(l1, l2):
        dummy = Node(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = Node(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



    def rotate_list(head, k):
        if not head or not head.next:
            return head
        
        # Find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Connect tail to head (circular)
        tail.next = head
        k = k % length
        
        # Find new head
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head


    # def sort_list(head):
    #     if not head or not head.next:
    #         return head
        
    #     # Split list into halves
    #     slow, fast = head, head.next
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     mid = slow.next
    #     slow.next = None
        
    #     left = sort_list(head)
    #     right = sort_list(mid)
        
    #     return merge_lists(left, right)  # using merge_lists from problem #4
