def count_sort(li,maxcount = 20):
    count = [0 for i in range(maxcount+1)]
    for val in li:
        count[val] += 1
    ans = []
    for  ind,val in enumerate(count):
        for i in range(val):
            ans.append(ind)
    print(ans)
    return ans

import random
li = [random.randint(0,10) for i in range(20)]
print(li)
print(li.count(3))
count_sort(li)

