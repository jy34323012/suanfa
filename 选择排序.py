a=[3,294,4,5,276,23,24]

# a =[6,5,12,4,52,13,13354]

def select(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]
select(a)
print(a)



