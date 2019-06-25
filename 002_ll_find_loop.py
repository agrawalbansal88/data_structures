from basic_link_link import List, Node

def find_loop(lis):
    if not lis.head: return False
    slow_path = lis.head
    fast_path = lis.head.next
    while slow_path and fast_path and fast_path.next:
        if slow_path == fast_path: return True
        fast_path = fast_path.next.next
        slow_path = slow_path.next
    return False


def remove_loop(lis):
    cleaned_list = []
    temp = lis.head
    prev = None
    while temp:
        if temp in cleaned_list:
            print "Loop entry point found", temp.data, "removing loop"
            prev.next = None
            break
        else:
            cleaned_list.append(temp)
            prev = temp
            temp = temp.next

lis = List()
lis.bulk_insert([1, 2, 3, 4, 5])
lis.print_list()

loop = Node(6)
loop.next = Node(7)
loop.next.next = Node(8)
loop.next.next.next = Node(9)
loop.next.next.next.next = lis.head.next.next
lis.insert_node(loop)
if find_loop(lis):
    print "loop found"
    remove_loop(lis)
#lis.print_detailed_data()
lis.print_list()
