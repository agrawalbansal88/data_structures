from basic_list import List, Node

class ReverseSupportedLinkList(List):
    def find_loop(self):
        if self.head is None or self.head.next is None: return # no loop

        p1 = self.head
        p2 = self.head.next
        while p1 is not None and  p2 is not None:
            if p1.next is None or p2.next is None or p2.next.next is None: break
            if p1.next == p2.next.next:
                print "Loop found"
                self.fix_loop(p2)
                break
            p1 = p1.next
            p2 = p2.next.next

    def fix_loop(self, p2):
        n_p1 = self.head
        while 1:
            n_p2 = p2
            while n_p2.next!=p2 and n_p1 != n_p2.next:
                n_p2 = n_p2.next
            if n_p1 == n_p2.next:
                break
            n_p1 = n_p1.next
        n_p2.next = None



ek_list = ReverseSupportedLinkList()
loop_node = Node(10)
alist = Node(1)
ek_list.head = alist
alist.next = Node(2)
alist.next.next = loop_node
alist.next.next.next = Node(4)
alist.next.next.next.next = Node(5)
alist.next.next.next.next.next = Node(6)
alist.next.next.next.next.next.next = loop_node
ek_list.find_loop()
ek_list.print_list()

