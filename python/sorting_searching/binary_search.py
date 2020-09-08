
def find_element(arr, value, l, r):
    mid = (l+r)/2
    print l, mid, r
    if r-l==1 and arr[r] != value and arr[l] != value:
        return None

    if arr[mid] > value:
        print "lower called"
        return find_element(arr, value, l, mid)
    elif arr[mid] < value:
        print "upper called"
        return find_element(arr, value, mid, r)
    else:
        print "value {} found at position {}".format(value, mid)
        return mid

arr = [1,2,4,5,7,8,12,13,16,22,34,54,100]
print arr
position = find_element(arr, 8, 0, len(arr)-1)
print "Position ", position
