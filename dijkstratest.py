# 狄克斯特拉算法
# 求A->B最短且耗时最短距离

# 同时存储邻居和前往邻居的开销
graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['final'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['final'] = 5

graph['final'] = {}

# 存储每个节点的开销
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['final'] = infinity

# 存储父节点的字典
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['final'] = None

# 记录处理过的节点
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    # 找出开销最低的节点
    node = find_lowest_cost_node(costs)
    while node is not None:
        # 获取该节点开销
        cost = costs[node]
        # 获取该节点邻居
        neighbors = graph[node]
        # 遍历邻居
        for n in neighbors.keys():
            # 距离
            new_cost = cost + neighbors[n]
            # 找到更短距离
            if costs[n] > new_cost:
                # 更新节点开销
                costs[n] = new_cost
                # 更新节点的父节点
                parents[n] = node
        # 将处理过的节点放入列表中
        processed.append(node)
        # 继续循环
        node = find_lowest_cost_node(costs)
    # 打印最短开销
    print(costs['final'])


dijkstra()
