def quick_sort_standord(array, low, high):
    if low < high:
        key_index = partion(array, low, high)
        quick_sort_standord(array, low, key_index-1)
        quick_sort_standord(array, key_index + 1, high)


def partion(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


if __name__ == '__main__':
    array2 = [9, 3, 2, 1, 4, 6, 7, 0, 5]

    print(array2)
    quick_sort_standord(array2, 0, len(array2) - 1)
    print(array2)

# def quickSort(arr):
#     return qsort(arr, 0, len(arr)-1)

# def qsort(arr, left, right):
#     if left >= right: # 递归结束条件，当区间里只有一个元素时，不用排序直接返回
#         return
#     k = arr[left] # 基准数
#     i = left
#     j = right
#     while i != j:
#         while arr[j] > k and i < j: # 顺序很重要，要先从右边开始找（最后交换基准时换过去的数要保证比基准小，因为基准选取数组第一个数，在小数堆中） （保证和基准数交换的数小于基准数，因为交换后该数在左边。）
#             j -= 1
#         while arr[i] <= k and i < j:
#             i += 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     # 将基准数归位
#     arr[left], arr[i] = arr[i], arr[left]
#     qsort(arr, left, i-1) # 递归左边
#     qsort(arr, i+1, right) # 递归右边
#     return arr


