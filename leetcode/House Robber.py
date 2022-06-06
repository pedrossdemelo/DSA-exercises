# https://leetcode.com/problems/house-robber/

def rob(houses):
    if len(houses) <= 2:
        return max(houses, default=0)

    best_loot_starting_at = [0] * (len(houses) - 2) + [max(houses[-2:])] + [houses[-1]]
    current_house = len(houses) - 3
    while current_house >= 0:
        current_loot = houses[current_house]
        best_loot_starting_at[current_house] = max(
            current_loot + best_loot_starting_at[current_house + 2],
            best_loot_starting_at[current_house + 1],
        )
        current_house -= 1

    return best_loot_starting_at[0]
