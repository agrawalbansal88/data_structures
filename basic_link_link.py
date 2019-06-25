class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if data is None:
            raise "None data received"
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp:
            if not temp.next:
                temp.next = Node(data)
                return
            else:
                temp = temp.next

    def insert_node(self, node):
        if node is None:
            raise "None data received"
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp:
            if not temp.next:
                temp.next = node
                return
            else:
                temp = temp.next


    def bulk_insert(self, list_data):
        for data in list_data:
            self.insert(data)

    def get_data(self):
        data = []
        temp = self.head
        while temp:
            data.append(temp.data)
            temp = temp.next
        return data

    def print_list(self):
        print self.get_data()

    def print_detailed_data(self):
        temp = self.head
        while temp:
            print temp.data, temp
            temp = temp.next


