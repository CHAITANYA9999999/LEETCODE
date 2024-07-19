class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=n
        for i in range(2,n+1):
            for j in range(n-i+1):
                string = s[j:j+i]
                if string == string[::-1]:
                    count+=1
        return count