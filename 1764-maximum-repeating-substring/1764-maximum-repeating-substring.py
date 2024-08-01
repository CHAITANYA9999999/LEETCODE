class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        prev = ""
        temp = word
        while True:
            if temp not in sequence: return len(prev)//len(word)
            prev = temp
            temp += word
        return len(prev)//len(word)