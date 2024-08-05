import re

class Solution:
    def reverseWords(self, s: str) -> str:
        l = re.split('\s',re.sub(r"\s+", " ", s.strip()))
        l.reverse()
        return " ".join(l)