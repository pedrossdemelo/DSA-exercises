# https://leetcode.com/problems/expressive-words/

# s = len(s) | n = len(words) | m = avg len(words[i])
# Time: O(s + nm) | Space: O(s + nm)
def expressiveWords(s, words):
    def compress(word):
        word = list(word)
        start = end = 0
        while start < len(word):
            end = start
            while end < len(word) and word[start] == word[end]:
                end += 1
            repetitions = end - start
            if repetitions == 1:
                word[start:end] = [word[start], 1]
                start += 1
            if repetitions > 1:
                word[start+1:end] = [repetitions]
                start += 1
            start += 1
        return word
    s = compress(s)
    words = [compress(word) for word in words]
    matches = 0

    for compressed in words:
        if len(compressed) != len(s):
            continue

        for i in range(0, len(s), 2):
            sletter, samount = s[i], s[i+1]
            letter, amount = compressed[i], compressed[i+1]
            if letter != sletter: break
            if amount > samount: break
            if amount < samount and samount < 3: break
            if i == len(s) - 2:
                matches += 1

    return matches


words = ["zzyy", "zy", "zyy"]
s = "zzzzzyyyyy"

print(expressiveWords(s, words))
