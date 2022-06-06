# https://leetcode.com/problems/combination-sum/

from collections import defaultdict
from math import gcd
# UNFINISHED


def combinationSum(candidates, target):
    combinations_with_sum = defaultdict(list)
    step_size = gcd(*candidates, target)

    for curr_step in range(step_size, target + 1, step_size):
        for candidate in candidates:
            diff = curr_step - candidate
            if diff < 0:
                continue
            if diff == 0:
                combinations_with_sum[curr_step].append([candidate])
            if diff > 0 and combinations_with_sum[diff]:
                for combination in combinations_with_sum[diff]:
                    if len(combination) + 1 not in [
                        len(comb) for comb in combinations_with_sum[curr_step]
                    ]:
                        combinations_with_sum[curr_step].append(
                            combination + [candidate]
                        )

    return combinations_with_sum[target]


print(combinationSum([2, 3, 6], 7))
