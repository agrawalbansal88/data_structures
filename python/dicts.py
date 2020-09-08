
def  isPossible(arr):

    leng = len(arr)
    i =0
    while i<leng:
        if arr[i]== 0:
            return False
        if arr[i] +i > leng-1:
            return False
        if arr[i] +i == leng-1:
            return True
        i+=arr[i]



print isPossible([3, 0, 1, 2, 1, 1])
print isPossible([1, 1, 1, 5, 1])