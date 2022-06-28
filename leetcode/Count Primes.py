# https://leetcode.com/problems/count-primes/

from math import ceil, sqrt


def countPrimes(n):
    if n <= 2: return 0
    primes = [2]
    # first we get the primes between 3 and sqrt(n)
    for num in range(3, ceil(sqrt(n)), 2):
        if any(num % prime == 0 for prime in primes):
            continue
        primes.append(num)

    # then we subtract all nums from range(2, n) that are divible by our primes
    nonprimes = set()
    for prime in primes:
        for num in range(2 * prime, n, prime):
            nonprimes.add(num)

    return n - 2 - len(nonprimes)

print(countPrimes(50))
