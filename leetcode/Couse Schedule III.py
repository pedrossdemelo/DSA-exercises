# https://leetcode.com/problems/course-schedule-iii/

import heapq

# Time: O(nlogn) | Space: (n)
def scheduleCourse(courses):
    courses.sort(key=lambda x: x[1])
    maxheap = []
    day = courses_taken = 0
    for duration, last_day in courses:
        heapq.heappush(maxheap, -duration)
        day += duration
        courses_taken += 1
        if day > last_day:
            day -= -heapq.heappop(maxheap)
            courses_taken -= 1
    return courses_taken

courses = [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
print(scheduleCourse(courses))