def shell_sort(items):
    """
    希尔排序
    :param items:
    :return:
    """
    n = len(items)
    step = n // 2
    while step > 0:
        for cur in range(step, n):
            i = cur
            while i >= step and items[i-step] > items[i]:
                items[i - step], items[i] = items[i], items[i-step]
                i -= step
        step = step // 2

li = [5,7,4,6,3,1,2,9,8]
shell_sort(li)
print(li)