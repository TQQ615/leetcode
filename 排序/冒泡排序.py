def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubbleSort([5,1,7,5,1,0,8,9]))

# 复杂度分析：O(n^2)
# 相关分析：https://www.runoob.com/w3cnote/bubble-sort.html
