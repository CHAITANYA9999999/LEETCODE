class Solution(object):
    def isVowel(self,s):
        return s=="a" or s=="e" or s=="i" or s=="o" or s=="u"
    
    def maxVowels(self, s, k):
        max_count=0
        l=list(s)
        for i in range(k):
            if self.isVowel(s[i]):
                max_count+=1
        count=max_count
        for i in range(k,len(s)):
            if self.isVowel(s[i]):
                count+=1
            if self.isVowel(s[i-k]):
                count-=1
            max_count=max(max_count,count)
        return max_count