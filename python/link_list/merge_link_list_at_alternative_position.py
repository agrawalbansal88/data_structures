from basic_list import List
class AddList(List):
    def merge(self, other_list):
        list1 =  self.head
        list2 = other_list.head

        while list1 is not None:
            list1_next = list1.next
            if list2:
                list2_next = list2.next
                list1.next = list2
                list1.next.next = list1_next
                list2 = list2_next
                list1 = list1.next.next
            else:
                break
        other_list.head = list2


list1 =  AddList()
list1.bulk_insert([5,6,3,11])
list2 =  AddList()
list2.bulk_insert([8,4])

list1.print_list()
list2.print_list()

list1.merge(list2)

list1.print_list()
list2.print_list()

