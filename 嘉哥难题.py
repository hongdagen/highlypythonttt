'''
str1 -> str2 最少步骤  插替删
'''

count = 0


def test(str1, str2):
    list_str1 = [i for i in str1]
    list_str2 = [i for i in str2]
    while True:
        if len(list_str1) != len(list_str2):
            if len(list_str1) < len(list_str2):
                result = add_func(list_str1, list_str2)
                return 'str1:%s,count:%d' % (result, count)
            else:
                result = del_func(list_str1, list_str2)
                return 'str1:%s,count:%d' % (result, count)
        else:
            result = func(list_str1, list_str2)
            break
    return 'str1:%s,count:%d' % (result, count)


def func(list1, list2):
    i = 0
    j = 0
    global count
    while i < len(list1):
        while j < len(list2):
            if list1[i] != list2[j]:
                list1[i] = list2[j]
                j += 1
                i += 1
                count += 1
            else:
                j += 1
                i += 1

    return ''.join([k for k in list1])


def add_func(list1, list2):
    i = 0
    j = 0
    global count
    while i < len(list1):
        while j < len(list2):
            if list1[i] == list2[j]:
                j += 1
                i += 1
                break
            else:
                list1[i] = list2[j]
                j += 1
                i += 1
                count += 1
                break
    length = len(list2) - len(list1)
    k = 0
    while k < length:
        list1.append(list2[-length + k])
        k += 1
        count += 1
    return ''.join([x for x in list1])


def del_func(list1, list2):
    i = 0
    j = 0
    global count
    while j < len(list2):
        while i < len(list1):
            if list1[i] == list2[j]:
                j += 1
                i += 1
                break
            else:
                list1[i] = list2[j]
                j += 1
                i += 1
                count += 1
                break
    length = len(list1) - len(list2)
    k = 0
    while k < length:
        list1.remove(list1[-length + k])
        k += 1
        count += 1
    return ''.join([x for x in list1])


print(test('aabcd', 'abcd'))
