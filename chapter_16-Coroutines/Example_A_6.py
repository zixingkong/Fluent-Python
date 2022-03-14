# -*- coding: utf-8 -*-
"""
Taxi simulator
==============
Driving a taxi from the console::
    >>> from taxi_sim import taxi_process
    >>> taxi = taxi_process(ident=13, trips=2, start_time=0)
    >>> next(taxi)
    Event(time=0, proc=13, action='leave garage')
    >>> taxi.send(_.time + 7)
    Event(time=7, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 23)
    Event(time=30, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 5)
    Event(time=35, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 48)
    Event(time=83, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=84, proc=13, action='going home')
    >>> taxi.send(_.time + 10)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
Sample run with two cars, random seed 10. This is a valid doctest::
    >>> main(num_taxis=2, seed=10)
    taxi: 0 Event(time=0, proc=0, action='leave garage')
    taxi: 0 Event(time=5, proc=0, action='pick up passenger')
    taxi: 1 Event(time=5, proc=1, action='leave garage')
    taxi: 1 Event(time=10, proc=1, action='pick up passenger')
    taxi: 1 Event(time=15, proc=1, action='drop off passenger')
    taxi: 0 Event(time=17, proc=0, action='drop off passenger')
    taxi: 1 Event(time=24, proc=1, action='pick up passenger')
    taxi: 0 Event(time=26, proc=0, action='pick up passenger')
    taxi: 0 Event(time=30, proc=0, action='drop off passenger')
    taxi: 0 Event(time=34, proc=0, action='going home')
    taxi: 1 Event(time=46, proc=1, action='drop off passenger')
    taxi: 1 Event(time=48, proc=1, action='pick up passenger')
    taxi: 1 Event(time=110, proc=1, action='drop off passenger')
    taxi: 1 Event(time=139, proc=1, action='pick up passenger')
    taxi: 1 Event(time=140, proc=1, action='drop off passenger')
    taxi: 1 Event(time=150, proc=1, action='going home')
    *** end of events ***
See longer sample run at the end of this module.
"""
import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5
Event = collections.namedtuple('Event', 'time proc action')


# BEGIN TAXI_PROCESS
def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change
    ident: 出租车的编号
    trips: 出租车回家之前的行程数量,即载客次数
    start_time: 出租车离开车库的时间
    """
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')
    # end of taxi process
    # END TAXI_PROCESS


# BEGIN TAXI_SIMULATOR
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """Schedule and display events until time is up"""
        # schedule the first event for each cab
        #  迭代表示各辆出租车的进程。
        # a. 在各辆出租车上调用 next() 函数，预激协程。这样会产出各辆出租车的第一个事件。
        # b. 把各个事件放入 Simulator 类的 self.events 属性（队列）中
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
        # main loop of the simulation
        #  满足 sim_time < end_time 条件时，运行仿真系统的主循环。
        # a. 检查 self.events 属性是否为空；如果为空，跳出循环。
        # b. 从 self.events 中获取当前事件（current_event），即 PriorityQueue 对象中时间值最
        # 小的 Event 对象。
        # c. 显示获取的 Event 对象。
        # d. 获取 current_event 的 time 属性，更新仿真时间。
        # e. 把时间发给 current_event 的 proc 属性标识的协程，产出下一个事件（next_event）。
        # f. 把 next_event 添加到 self.events 队列中，排定 next_event。
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * ' ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
        # END TAXI_SIMULATOR


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling 5
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip  20
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1 / interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # get reproducible results
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
             for i in range(num_taxis)}

    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description='Taxi fleet simulator.')
    # parser.add_argument('-e', '--end-time', type=int,
    #                     default=DEFAULT_END_TIME,
    #                     help='simulation end time; default = %s'
    #                          % DEFAULT_END_TIME)
    # parser.add_argument('-t', '--taxis', type=int,
    #                     default=DEFAULT_NUMBER_OF_TAXIS,
    #                     help='number of taxis running; default = %s'
    #                          % DEFAULT_NUMBER_OF_TAXIS)
    # parser.add_argument('-s', '--seed', type=int, default=None,
    #                     help='random generator seed (for testing)')
    # args = parser.parse_args()
    # main(args.end_time, args.taxis, args.seed)
    main(seed=3)
