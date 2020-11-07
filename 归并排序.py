# def merge(li,low,mid,high):
#     i = low
#     j = mid +1
#     ltmp = []
#     while i<=mid and j<=high:
#         if li[i]<li[j]:
#             ltmp.append(li[i])
#             i +=1
#         else:
#             ltmp.append(li[j])
#             j +=1
#     while i <=mid:
#         ltmp.append(li[i])
#         i += 1
#     while j <=high:
#         ltmp.append(li[j])
#         j += 1
#     print(ltmp)
#     # li1=[]
#     # li1[0:7]=ltmp
#     # print(li1)
#     print(low, high)
#     print(li)
#     li[0:7]=ltmp
#     # li[low:high] = ltmp
#     print(li)
#     print(len(li))
#
# li = [2, 4, 5, 7, 1, 3]
# merge(li,0,3,5)




def merge1(lis):
    start = 0
    mid = len(lis)//2
    end = len(lis)
    ltmp = []
    lis1=lis[0:mid]
    lis2=lis[mid:end]
    while len(lis1)>0 and len(lis2)>0:
        if lis1[0] <=lis2[0]:
            ltmp.append(lis1.pop(0))
        else:
            ltmp.append(lis2.pop(0))
    ltmp += lis1
    ltmp += lis2
    print(ltmp)


li = [2, 4, 5, 0, 1, 3]
merge1(li)

