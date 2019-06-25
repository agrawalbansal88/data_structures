class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def bulk_insert(self, values):
        for value in values:
            self.insert(Node(value))

    def insert(self, value):
        if self.head is None:
            self.head = value
        else:
            header = self.head
            while header.next is not None:
                header = header.next
            header.next = value

    def print_list(self):
        header = self.head
        while header is not None:
            print header.data
            header = header.next
        print

    def delete_entry(self, value):
        print "Trying to delete ", value
        header = self.head
        prev = None
        if header is None: print "List is empty" ;return
        if header.data == value:print "Removing item", header.data;self.head=None;return

        while header is not None:
            if header.data != value:
                prev = header
                header = header.next
            else:
                print "Removing item", header.data
                prev.next = header.next
                return

        print "Item not found"

    def delete_entry_simple(self, value):
        header = self.head
        prev = None
        if header is not None and header.data == value:
            self.head = self.head.next
            return True

        while header is not None:
            if header.data != value:
                prev = header
                header = header.next
            else:
                prev.next = header.next
                return True
        return False

    def length(self):
        length = 0
        head = self.head
        while head is not None:
            head = head.next
            length += 1
        return length


if __name__ =='main':
    l_list = List()
    l_list.delete_entry_simple(20)
    l_list.insert(Node(10))
    l_list.insert(Node(20))
    l_list.insert(Node(30))
    l_list.insert(Node(40))

    l_list.print_list()
    l_list.delete_entry_simple(10)
    l_list.print_list()
