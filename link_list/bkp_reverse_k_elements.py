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

        if count !=1:
            end_point.next = prev
            end_point = first_end

        self.head = start_point
        end_point.next = None

alist = ReverseSupportedLinkList()
alist.bulk_insert([1,2,3,4,5,6,7,8,9,10,11])
alist.print_list()
alist.reverse(3)
alist.print_list()

