#sortinf dll
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

    def sort_DLL(self):
        def merge_sort(head):
            if not head or not head.next:
                return head

            # --- Split into two halves ---
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            second = slow.next
            slow.next = None
            if second:
                second.prev = None

            # --- Recursive sort ---
            left = merge_sort(head)
            right = merge_sort(second)

            # --- Merge two sorted halves ---
            return merge(left, right)

        def merge(first, second):
            if not first: return second
            if not second: return first

            if first.value <= second.value:
                first.next = merge(first.next, second)
                if first.next:
                    first.next.prev = first
                return first
            else:
                second.next = merge(first, second.next)
                if second.next:
                    second.next.prev = second
                return second

        # --- Run merge_sort on DLL ---
        if not self.head or not self.head.next:
            return "DLL is empty or has one node"

        self.head = merge_sort(self.head)

        # --- Reset tail pointer ---
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr


    def traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            curr = self.head
            while curr:
                print(curr.value, end="-><-")
                curr = curr.next
            print("None")


d = DLL()
d2 = DLL()

l = [3,2,4,5,7,2,3,1]
sorted(l)

for i in range(len(l)):
    d2.append(i)

for i in [6,5,4,3,2,1]:
    d.append(i)


d.traverse()
d.sort_DLL()
d.traverse()



d2.traverse()
d2.sort_DLL()
d2.traverse()
