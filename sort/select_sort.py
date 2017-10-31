def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    li = [423, 2, 142, 43, 56, 75]

    select_sort(li)
    print(li)
