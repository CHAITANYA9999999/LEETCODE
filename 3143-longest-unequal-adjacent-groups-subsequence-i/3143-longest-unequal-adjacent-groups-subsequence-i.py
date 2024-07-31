class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        n = len(words)
        cur_bit = groups[0]
        res.append(words[0])
        for i in range(1,n):
            if groups[i] != cur_bit:
                res.append(words[i])
                cur_bit = groups[i]
        return res