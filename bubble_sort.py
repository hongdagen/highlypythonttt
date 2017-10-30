"""冒泡排序"""


def bubble_sort(alist):
    for j in range(len(alist) - 1):
        for i in range(0, len(alist) - 1 - j):
            if alist[i + 1] < alist[i]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


li = [54, 12, 542, 14, 5, 123, 566]
bubble_sort(li)
print(li)
