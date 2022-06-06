# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from collections import defaultdict


def groupThePeople(groupSizes):
    groups = defaultdict(list)
    res = []

    for i, gsize in enumerate(groupSizes):
        groups[gsize].append(i)

    for gsize, indexes in groups.items():
        arrays_amount = len(indexes) // gsize

        for _ in range(arrays_amount):
            temp = []
            for _ in range(gsize):
                temp.append(indexes.pop())
            res.append(temp)

    return res


print(groupThePeople([3,3,3,3,3,1,3]))