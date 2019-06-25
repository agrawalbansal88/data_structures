class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class List():
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while (tmp):
            print tmp.value,
            tmp = tmp.next
        print "\n"

    def addNode(self, value):
        if not self.head:
            self.head = Node(value)
            return
        tmp= self.head
        while(tmp.next):
            tmp=tmp.next
        tmp.next = Node(value)

    def bulk_insert(self, values):
        for value in values:
            self.addNode(value)

    def reverse(self):
        prev = None
        curr = self.head
        while(curr):
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        self.head = prev


link = List()
link.bulk_insert([1,2,3,4,5,6])
link.addNode(7)
link.addNode(8)
link.printList()
link.reverse()
link.printList()
