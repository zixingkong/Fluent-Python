# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     greedy_algorithm
   Description : 贪婪算法
   date：          2022/2/5
-------------------------------------------------
"""

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    # states_covered：该广播台覆盖的所有未覆盖的州
    states_covered = set()
    # 每次for循环找到覆盖了最多的未覆盖州的广播台
    for station, states in stations.items():
        # covered：当前广播台覆盖的还未覆盖的一系列州
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)