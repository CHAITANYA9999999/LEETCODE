class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(s,i,j):
            l = i
            r = j
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def helper(i):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    path.append(s[i:j+1])
                    helper(j+1)
                    path.pop()
        helper(0)
        return res