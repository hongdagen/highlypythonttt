'''sum(2,4,6)递归'''

'''
def sum_fact(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        result = list_num.pop(0) + sum_fact(list_num)
        return result


print(sum_fact([1, 3, 4, 9]))
'''


# 快速排序
def quick_sort(list_unsort):
    if len(list_unsort) < 2:
        return list_unsort
    else:
        pivot = list_unsort[0]
        less = [i for i in list_unsort[1:] if i <= pivot]
        greater = [i for i in list_unsort[1:] if i >= pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 2, 4, 1, 5, 6]))
