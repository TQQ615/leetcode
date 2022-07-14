def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n / 2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    relt = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            relt.append(left[0])
            left.pop(0)
        else:
            relt.append(right[0])
            right.pop(0)
    if len(left) > 0:
        relt += left
    if len(right) > 0:
        relt += right
    return relt


print(mergeSort([5,1,7,5,1,0,8,9]))

# O(nlogn)，稳定
