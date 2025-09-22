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
        new_node=Node(value)
        if self.head is None:
            self.head =new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        

    def delete_by_value(self, value):
        if self.head is None:
            return "DLL is empty"
        if self.head.next is None:
            self.head =None

        curr = self.head
        while curr:
            if curr.value == value:
                self.head.next = None
                self.head.next.prev = None
                self.head = self.head.next

    # def remove_duplicate(self):
    #     curr = self.head
    #     while curr and curr.next:
    #         if curr.value == curr.next.value:
    #             curr.next = curr.next.next
    #         else:
    #             curr = curr.next
            

    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return f"{curr.value}, found in dl_list"
            curr = curr.next
        else :
            return "search value not found"

    # # Sorted singly_linked_List
    # def remove_all_occurrences(self, value):
    #     curr = self.head
    #     while curr and curr.next :
    #         if curr.value == value:
    #             if curr.prev:
    #                 curr.prev.next = curr.next
    #             else:
    #                 self.head = curr.next
    #         curr = curr.next


    def extend_DLL(self, arr):
        for i in arr:
            self.append(i)

    def search_val_get_index(self, value):
        curr = self.head
        count = 0
        while curr:
            if curr.value == value:
                return f"search value{value} found at index {count}"             
            count += 1
            curr = curr.next
        return "search value not found"


    def get_index_by_value(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return "index out of range"

    def traverse(self):
        if self.head is None:
            print("DLL is empty")
        else:
            curr = self.head
            while curr:
                print(curr.value, end = "<->")
                curr = curr.next
            print("None")


    def remove_all_occurances(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
            curr = curr.next

    def remove_duplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next


d = DLL()
d.append(1)
d.append(1)
d.append(2)
d.append(3)
d.append(3)
d.append(4)
d.append(4)
d.append(5)
d.append(6)
d.traverse()

# d.delete_by_value(1)

# print(d.get_index_by_value(3))

# d.remove_duplicate()

# d.remove_all_occurrences(3)

# d.extend_DLL(['x', 'y', 'z', 'q', 'w', 'e'])

# print(d.search(4))

# d.remove_all_occurances(5)

d.remove_duplicates()

d.traverse()
