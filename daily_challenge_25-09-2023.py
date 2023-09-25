from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count=Counter(s)
        t_count=Counter(t)
        for alp in t_count.keys():
            if alp not in s_count or t_count[alp]!=s_count[alp]:
                return alp