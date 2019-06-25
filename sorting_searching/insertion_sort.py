# pick 1 and compare with all

arr = [4,2,6,1,22,42,55,-9, -11, 34]
ln = len(arr)
print arr
for i in range(ln-1):
    for j in range(i+1, ln):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print arr
