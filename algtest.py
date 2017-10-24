# 广度优先算法
# “广度优先搜索指出是否有从A到B的路径。如果有，广度优先搜索将找出最短路径。”

from collections import deque

graph = dict()
graph["qw"] = ["aa", "bb", "mm"]
graph["cd"] = []
graph["im"] = []
graph["aa"] = ["nm"]
graph["bb"] = ["cc", "gg"]
graph["mm"] = []
graph["cc"] = []
graph["gg"] = []
graph["nm"] = []


def find_seller():
    # 创建一个队列
    search_queue = deque()
    # 把人加入到搜索队列
    search_queue += graph.keys()
    # 记录检查过的人
    searched = []

    while search_queue:
        # 取出第一个人
        person = search_queue.popleft()
        # 调用person_is_seller函数 如果是 返回true
        if person_is_seller(person) and person not in searched:
            print('%s is seller' % person)
            searched.append(person)
        # 如果不是 将这个人的朋友加入到队列
        else:
            search_queue.extend(graph[person])
            searched.append(person)
    # 如果都没有 return false
    return


def person_is_seller(name):
    str_name = ''.join([i for i in name])
    if str_name[-1] == 'm':
        return True


if __name__ == '__main__':
    find_seller()
