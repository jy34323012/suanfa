# def merge_sort(list1):
#     if len(list1) ==1:
#         return list1
#     mid = len(list1)//2
#     left = list1[:mid]
#     right = list1[mid:]
#     l1 = merge_sort(left)
#     l2 = merge_sort(right)
#     print(l1)
#     print(l2)
#
# list1 = [6, 5, 3, 1, 8, 7, 2, 4]
# merge_sort(list1)

def mergesort(alist):
    if len(alist)<=1:
        return alist
    mid=len(alist)//2
    left=mergesort(alist[:mid])
    # print("left= "+str(left))
    right=mergesort(alist[mid:])
    # print("right= "+str(right))
    return mergeSortedArray(left,right)
def mergeSortedArray(A,B):
    print('A: %s'+str(A))
    print('B: %s' + str(B))
    sortedArray=[]
    l=0
    r=0
    while l<len(A) and r<len(B):
        if A[l]<B[r]:
            sortedArray.append(A[l])
            l+=1
        else:
            sortedArray.append(B[r])
            r+=1
    sortedArray+=A[l:]
    sortedArray+=B[r:]
    return sortedArray
unsortedArray=[6, 5, 3, 1, 8, 7, 2, 4]
mergesort(unsortedArray)
a = mergesort(unsortedArray)
print(a)