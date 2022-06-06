# https://leetcode.com/problems/insert-interval/

def insert(intervals, newInterval):
    new_s, new_e = newInterval
    start, end = min(intervals[0][0], new_s), max(intervals[-1][-1], new_e)
    board = {time:0 if time >= new_e or time < new_s else 2 for time in range(start, end + 1)}
    board[new_e] = 1

    for s, e in intervals:
        for t in range(s, e):
            board[t] = 2
        if not board[e]:
            board[e] = 1

    curr_start = None
    new_intervals = []
    for time, status in board.items():
        match status:
            # 0 = vacant, skip
            case 2: # used
                if curr_start == None:
                    curr_start = time

            case 1: # ending
                if curr_start != None:
                    new_intervals.append([curr_start, time])
                    curr_start = None
                else:
                    new_intervals.append([time, time])

    return new_intervals

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))