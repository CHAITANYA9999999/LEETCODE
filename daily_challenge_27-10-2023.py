class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx=0
        string=s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                st=s[i:j+1]
                # print(st,st[::-1])
                if st==st[::-1]:
                    if j-i+1>maxx:
                        maxx=j-i+1
                        string=st
                        print(string)
        return string
