# 贪婪算法

# 如何找出覆盖全美50个州的最小广播台集合
# 因获得精确解需要的时间太长，可以用近似算法
# 这个例子贪婪算法的运行事件O(n**2) n为广播台数量

# 创建列表 包含覆盖的州  转换为集合(去重)
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 广播台清单
stations = dict()
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# 存储最终选择的广播台
final_stations = set()
# 存储覆盖了最多未覆盖州的广播台
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # covered包含当前广播台覆盖的一系列还未覆盖的州
        covered = states_needed & states_for_station
        # 检查该广播台覆盖的州是否比best_station多
        if len(covered) > len(states_covered):
            # 将best_station设置为当前广播台
            best_station = station
            states_covered = covered
        # 更新州 不在复用
        states_needed -= states_covered
        # 添加到最终广播台
        if best_station != None:
            final_stations.add(best_station)
print(final_stations)
