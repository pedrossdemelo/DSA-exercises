# https://leetcode.com/problems/car-fleet/

# Time: O(n) | Space: O(n)
def carFleet(target, position, speed):
    etas = [(target - pos) / speed for pos, speed in sorted(zip(position, speed), reverse=True)]
    front, fleets = etas[0], 0

    for eta in etas[1:]:
        if eta <= front:
            continue
        fleets += 1
        front = eta

    return 1 + fleets

position = [10,8,0,5,3]
target = 12
speed = [2,4,1,1,3]

print(carFleet(target, position, speed))
