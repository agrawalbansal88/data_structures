from basic_list import List

class ReverseSupportedLinkList(List):
    def reverse(self, N):

        count = 1
        curr = self.head
        prev = None
        first_end = self.head
        start_point = None
        end_point = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
            if count == N:
                if start_point is None:
                    start_point = prev
                    end_point = first_end
                    first_end = next_
                else:
                    end_point.next = prev
                    end_point = first_end
                    first_end = next_
                count = 1
            else:
                count += 1
        if start_point is None:
            start_point = prev
            end_point = first_end
        elif count !=1:
            end_point.next = prev
            end_point = first_end

        self.head = start_point
        end_point.next = None

    def reverse_recursive(self, head, k):
        current = head 
        next  = None
        prev = None
        count = 0
         
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current . And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverse_recursive(next, k)
 
        # prev is new head of the input list
        return prev

alist = ReverseSupportedLinkList()
#alist.bulk_insert([1,2])
alist.bulk_insert([1,2,3,4,5,6,7,8,9,10,11])
alist.print_list()
alist.reverse(3)
alist.print_list()
alist.head = alist.reverse_recursive(alist.head, 3)
alist.print_list()
