def merge(arr1, arr2):
    tmp_arr = []
    while len(arr1) !=0 and len(arr2) !=0:
        if arr1[0] > arr2[0]:
            tmp_arr.append(arr2.pop(0))
        else:
            tmp_arr.append(arr1.pop(0))

    return tmp_arr + arr1 + arr2

def merge_sort(arr, start, end):
    if end-start <2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return arr[start:end+1]
    mid = (start+end)/2
    sorted_1 = merge_sort(arr, start, mid)
    sorted_2 = merge_sort(arr, mid+1, end)
    return merge(sorted_1, sorted_2)

def merge_without_extra_mem(arr, start, end):
    if end-start <2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return arr[start:end+1]
    mid = (start+end)/2
    merge_without_extra_mem(arr, start, mid)
    merge_without_extra_mem(arr, mid+1, end)
    merge_without(arr, start, mid, mid+1, end)

def merge_without(arr, start1, end1, start2, end2):
    tmp1 = arr[start1:end1+1]
    tmp2 = arr[start2:end2+1]
    while len(tmp1)!=0 and len(tmp2) !=0:
        if tmp1[0] > tmp2[0]:
            val = tmp2.pop(0)
        else:
            val = tmp1.pop(0)
        arr[start1] = val
        start1 += 1
    while len(tmp1)!=0:
        arr[start1] = tmp1.pop(0)
        start1 += 1

    while len(tmp2)!=0:
        arr[start1] = tmp2.pop(0)
        start1 += 1



arr= [1,4,-2,3,44,23,-23,99,109,-2221,32]
print arr
print
#arr= merge_sort(arr, 0, len(arr)-1)
merge_without_extra_mem(arr, 0, len(arr)-1)
print arr
