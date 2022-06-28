# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

from heapq import heappop, heappush, heapreplace

class inversestr:
    def __init__(self, string) -> None:
        self.string = str(string)
    def __lt__(self, other):
        return self.string > str(other)
    def __gt__(self, other):
        return self.string < str(other)
    def __str__(self) -> str:
        return self.string
    def __repr__(self) -> str:
        return self.string


class SORTracker:
    def __init__(self):
        self.best = []
        self.rest = []

    def add(self, name: str, score: int) -> None:
        s, n = self.best[0] if self.best else (None, None)
        if s and (score, inversestr(name)) > (s, n):
            demotedscore, demotedname = heapreplace(self.best, (score, inversestr(name)))
            heappush(self.rest, (-demotedscore, str(demotedname)))
        else:
            heappush(self.rest, (-score, name))

    def get(self) -> str:
        promotedscore, promotedname = heappop(self.rest)
        heappush(self.best, (-promotedscore, inversestr(promotedname)))
        return str(self.best[0][1])


methods, args, expected = (
    [
        "SORTracker",
        "add",
        "add",
        "get",
        "add",
        "get",
        "add",
        "get",
        "add",
        "get",
        "add",
        "get",
        "get",
    ],
    [
        [],
        ["bradford", 2],
        ["branford", 3],
        [],
        ["alps", 2],
        [],
        ["orland", 2],
        [],
        ["orlando", 3],
        [],
        ["alpine", 2],
        [],
        [],
    ],
    [
        None,
        None,
        None,
        "branford",
        None,
        "alps",
        None,
        "bradford",
        None,
        "bradford",
        None,
        "bradford",
        "orland",
    ],
)

solution = SORTracker(*args[0])

for method, arg, expect in zip(methods[1:], args[1:], expected[1:]):
    arguments = ", ".join([str(a) for a in arg])
    print(f"{method}({arguments})")
    res = getattr(solution, method)(*arg)
    print(f"{res} | {expect}")
