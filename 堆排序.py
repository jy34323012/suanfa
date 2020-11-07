def sift(li,low,high):
    # 向下调整
    #li  ： 列表
    #low : 堆根节点位置
    #high: 堆 最后一个元素的位置
    # j 左孩子
    i = low
    j=2*i+1
    tmp = li[low]
    while j <=high:   #只要j有数
        if j+1 <= high and li[j+1] > li[j]:   #如果右孩子比较大
            j = j + 1
        if li[j]>tmp:
            li[i] = li[j]
            i = j                   #往下看一层
            j = 2*i +1
        else:               #tmp 更大  把tmp 放到 I的位置上
            li[i]  =  tmp
            break
    else:
        li[i] = tmp    #把tmp放到叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1)
    # for i in range(n-1,-1,-1):
    #     #i 指向堆得最后一个元素
    #     li[0],li[i] = li[i],li[0]
    #     sift(li,0,i-1)    #i-1是新的high
    print(li)

list1 = [i for i in range(10)]
import random
random.shuffle(list1)
print(list1)
heap_sort(list1)
print(list1)

