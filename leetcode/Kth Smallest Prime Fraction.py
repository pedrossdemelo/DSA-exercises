import heapq

# Time: O(klogn) | Space: O(n)
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    heap = [(arr[i] / arr[-1], (i, n - 1)) for i in range(n - 1)]

    for _ in range(k - 1):
        dividend_i, divisor_i = heap[0][1]
        divisor_i -= 1
        if dividend_i == divisor_i:
            heapq.heappop(heap)
        else:
            heapq.heapreplace(
                heap, (arr[dividend_i] / arr[divisor_i], (dividend_i, divisor_i))
            )

    dividend_i, divisor_i = heap[0][1]
    return [arr[dividend_i], arr[divisor_i]]


arr = [1, 2, 3, 5]
k = 7

print(kthSmallestPrimeFraction(arr, k))
