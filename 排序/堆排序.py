import math


def heapSort(arr):
    arr_len = len(arr)

    def heapify(arr, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < arr_len and arr[left] > arr[largest]:
            largest = left
        if right < arr_len and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(arr, largest)

    def buildHeap(arr):
        for i in range(len(arr) - 1, -1, -1):
            heapify(arr, i)

    buildHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr_len -= 1
        heapify(arr, 0)
    return arr


print(heapSort([5,1,7,5,1,0,8,9]))

"""
大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
堆排序的平均时间复杂度为 Ο(nlogn)

建堆过程：
对每个非叶子节点(n/2)都要调整一次大顶堆，一次调整需要经过log(n)次对比，总共nlog(n)
挑选之后调整最大堆：
每次选出第n大元素之后，重新调整调整log(n)，选出所有元素之后，一共调整nlog(n)

不稳定
"""