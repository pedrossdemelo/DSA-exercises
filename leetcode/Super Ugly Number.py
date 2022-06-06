# https://leetcode.com/problems/super-ugly-number/
# UNFINISHED

from re import S
from time import time

def nthSuperUglyNumber(n, primes):
    candidates = set(primes)

    start_time = time()
    current = 1
    for _ in range(1, n):
        candidates.discard(current)
        for prime in primes:
            new_candidate = prime * current
            if new_candidate not in candidates:
                candidates.add(new_candidate)
        current = min(candidates)

    print(f"Time elapsed: {time() - start_time}")
    return current

print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))
