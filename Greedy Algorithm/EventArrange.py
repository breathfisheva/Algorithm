'''
假设现在有N项工作，分别在 Si 时刻开始，在 Ti 时刻结束，对于每项工作可以选择做或者不做，但不可以同时选择时间重叠的工作（即使是开始的瞬间和结束的瞬间重叠也是不允许的）。要求尽可能的多做几件事，那么最多能做几件事呢？

3.3.1 分解问题：
当只有N'项工作的时候，如何选择哪一份工作满足工作时间不重叠，同时尽可能多做几件事。

3.3.2 选择最优策略：
策略1：选择开始时间最早的
策略2：选择活动时间最短的
策略3：选择结束时间最早的 (选择这个策略）
'''


class Event(object):
    def __init__(self, start, end):
        self.start = start
        self.end =end

def strategy(events): #找出剩下的events里最快结束的event， 用status来控制剩下的为0，选择的为1，选择了不合适的为2
    min_index = 0
    for i in range(1, len(events)):
        if events[i].end < events[min_index].end:
            min_index = i
    return min_index

def greedy(events, strategy):
    index = -1
    pre_event_end = 0

    while len(events) > 0:
        index = strategy(events)
        if (index!=-1):
            if events[index].start > pre_event_end:
                print("(%d,%d)" %(events[index].start, events[index].end))
                pre_event_end = events[index].end
            del events[index]


if __name__ == '__main__':
    events = [Event(12,14),Event(2,13),Event(8,12),Event(8,11),Event(6,10),Event(5,9),Event(3,8),Event(5,7),Event(0,6),Event(3,5),Event(1,4)]
    greedy(events,strategy)

