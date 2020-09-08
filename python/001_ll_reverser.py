from basic_link_link import List

def reverse_it_Iterative(lis):
    curr = lis.head
    prev, next = None, None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    lis.head = prev
    return lis

lis = List()
lis.insert(1)
lis.insert(4)
lis.bulk_insert([3, 12, 11, 9, 0])
lis.print_list()

lis = reverse_it_Iterative(lis)
lis.print_list()
