from basic_list import List

class ReverseSupportedLinkList(List):
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

    def reverse_recursive(self):
        if self.head is None: return
        self.reverseUtil(self.head, None)

    def reverseUtil(self, curr, prev):
        if curr.next is None : # If last node mark it head
            self.head = curr 
            curr.next = prev # Update next to prev node
            return
        next_ = curr.next # Save curr.next node for recursive call
        curr.next = prev # And update next
        self.reverseUtil(next_, curr)

alist = ReverseSupportedLinkList()
alist.bulk_insert([1,2,4,3,5])
alist.print_list()
alist.reverse()
alist.print_list()
alist.reverse_recursive()
alist.print_list()

