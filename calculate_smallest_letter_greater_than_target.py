class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target=='z' or target>=letters[-1]:
            return letters[0]
        try:
            i=letters.index(target)+1
        except:
            i=0
        while i<len(letters):
            if letters[i]>target:
                return letters[i]
            i+=1