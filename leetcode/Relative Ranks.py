# https://leetcode.com/problems/relative-ranks/submissions/

# Time: O(nlogn) | Space: O(n)
def findRelativeRanks(score):
    rank = sorted(((s, i) for i, s in enumerate(score)), reverse=True)
    medals = ["Gold", "Silver", "Bronze"]
    for i, (s, original_i) in enumerate(rank):
        score[original_i] = f"{medals[i]} Medal" if i < 3 else str(i + 1)
    return score