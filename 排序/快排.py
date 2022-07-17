# 递归版本
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    temp = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < temp:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSort(left) + [temp] + quickSort(right)


# 非递归版本
def quickSort2(arr):
    def quicksort(b, e):
        target = arr[b]
        while b < e:
            while b < e and arr[e] >= target:
                e -= 1
            arr[b] = arr[e]
            while b < e and arr[b] <= target:
                b += 1
            arr[e] = arr[b]
        arr[b] = target
        return b

    l = 0
    r = len(arr) - 1
    stack = [(l, r)]
    while len(stack) > 0:
        begin, end = stack.pop(0)
        idx = quicksort(begin, end)
        if idx > begin:
            stack.append((begin, idx - 1))
        if idx < end:
            stack.append((idx + 1, end))
    return arr


print(quickSort([5,1,7,5,1,0,8,9]))
print(quickSort2([5,1,7,5,1,0,8,9]))

# 时间复杂度：最坏：O(n^2) 平均：O(nlogn)， 不稳定（选最大可以满足稳定性的时候，选最小无法满足）
# 稳定性定义：
# 排序前后两个相等的数相对位置不变，则算法稳定。
