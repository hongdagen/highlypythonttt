# 动态规划   绘制并填充计算blue和clues最长公共子串的网格
str1 = "blue"
list_str1 = [i for i in str1]
str2 = "clue"
list_str2 = [i for i in str2]
j = 0
k = 0

if len(list_str1) < len(list_str2):
    for _ in range(len(list_str2) - len(list_str1)):
        list_str1.append(0)
elif len(list_str1) > len(list_str2):
    for _ in range(len(list_str1) - len(list_str2)):
        list_str2.append(0)

cell = [[0 for row in range(len(list_str1))] for col in range(len(list_str2))]
while j < len(list_str1):
    while k < len(list_str2):
        if list_str1[j] != list_str2[k]:
            cell[j][k] = 0
            j += 1
            k += 1
        else:
            cell[j][k] = cell[j - 1][k - 1] + 1
            j += 1
            k += 1

print(cell)
