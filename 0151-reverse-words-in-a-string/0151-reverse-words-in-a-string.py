import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))