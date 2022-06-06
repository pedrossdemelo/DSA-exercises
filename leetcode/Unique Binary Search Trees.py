# https://leetcode.com/problems/unique-binary-search-trees/


from collections import defaultdict


def numTress(nodes):
    unique_bsts_with = defaultdict(int)
    unique_bsts_with[0] = 1
    unique_bsts_with[1] = 1
    unique_bsts_with[2] = 2

    for current_amount in range(3, nodes + 1):
        child_nodes = current_amount - 1

        for amount_in_one_side in range(child_nodes // 2 + 1):
            amount_in_other_side = child_nodes - amount_in_one_side
            balanced = amount_in_one_side == amount_in_other_side
            unique_bsts = (
                unique_bsts_with[amount_in_one_side]
                * unique_bsts_with[amount_in_other_side]
            )
            unique_bsts_with[current_amount] += unique_bsts * (2 if not balanced else 1)

    return unique_bsts_with[nodes]

print(numTress(6))