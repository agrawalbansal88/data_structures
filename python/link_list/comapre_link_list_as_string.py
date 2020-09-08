from basic_list import List
class CompareList(List):
    def compare(self, other_list):
        list1 = self.head
        list2 = other_list.head
        while True:
            if list1 is None and list2 is None:
                return 0
            elif list1 is None:
                return -1
            elif list2 is None:
                return 1
            else:
                if list1.data > list2.data:
                    return 1
                elif list1.data < list2.data:
                    return -1
                else:
                    list1 = list1.next
                    list2 = list2.next

    def compare_new(self, other_list):
        list1 = self.head
        list2 = other_list.head
        while (list1 and list2 and list1.data == list2.data):
            list1 = list1.next
            list2 = list2.next

        if list1 and list2:
            return 1 if list1.data > list2.data else -1
        if list1 and not list2:
            return 1
        if not list1 and list2:
            return -1
        return 0


list1 = CompareList()
list2 = CompareList()
list1.bulk_insert(['g', 'e', 'e', 'j'])
list2.bulk_insert(['g', 'e', 'e', 'k'])
list1.print_list()
list2.print_list()
print list1.compare(list2)
print list1.compare_new(list2)
