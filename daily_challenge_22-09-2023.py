class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0
        for i in t:
            if k==len(s):
                return True
            if s[k]==i:
                k+=1
        return k==len(s)