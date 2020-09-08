from basic_list import List, Node

class IncresingOrderLinkList(List):
    def bulk_insert(self, values):
        for value in values:
            self.insert(value)
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node;return

        head = self.head
        if head.data > value:
            self.head = new_node
            self.head.next = head
        else:
            while head.next is not None and head.next.data < value:
                head = head.next
            new_node.next = head.next
            head.next = new_node

    def delete(self, value):
        if self.head is None: return
        head = self.head
        while head.next is not None and head.next.data != value:
            head = head.next

        if head.next is not None:
            head.next = head.next.next


alist = IncresingOrderLinkList()
alist.bulk_insert([4, 1,2,4,3,5, 6, 11,9, 2,3,20,1])
alist.print_list()
alist.delete(1)
alist.print_list()

