class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None


class KLinkedList:

    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_start(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_between(self, mid_node, val):
        new_node = Node(val)
        new_node.next = mid_node.next
        mid_node.next = new_node

    def remove(self, item_val):
        head_val = self.head
        if head_val is not None:
            if head_val.data_val == item_val:
                head_val = None
                return
            while head_val is not None:
                if head_val.data_val == item_val:
                    break
                prev = head_val
                head_val = head_val.next

            if head_val is None:
                return
            prev.next = head_val.next
            head_val = None

    def view_list(self):
        node = self.head
        while node:
            print(node.data_val)
            node = node.next


k_list = KLinkedList()
k_list.insert_start("test1")
k_list.insert_start("test2")
k_list.insert_start("test3")
k_list.insert_start("test4")
k_list.remove("test3")
k_list.view_list()





