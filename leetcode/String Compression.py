from typing import List

# Time: O(n) | Space: O(1)
def compress(chars: List[str]) -> int:
    start = end = 0
    while start < len(chars):
        end = start
        while end < len(chars) and chars[start] == chars[end]:
            end += 1
        repetitions = end - start
        if repetitions > 1:
            repetitions = str(repetitions)
            chars[start+1:end] = repetitions
            start += len(repetitions)
        start += 1
    return len(chars)

chars = ["p","p","p","p","m","m","b","b","b","b","b","u","u","r","r","u","n","n","n","n","n","n","n","n","n","n","n","u","u","u","u","a","a","u","u","r","r","r","s","s","a","a","y","y","y","g","g","g","g","g"]
print(compress(chars))
expect = ["p","4","m","2","b","5","u","2","r","2","u","n","1","1","u","4","a","2","u","2","r","3","s","2","a","2","y","3","g","5"]