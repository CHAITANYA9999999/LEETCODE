class Solution:
    def countAndSay(self, n: int) -> str:
        countandsay = ["1"]*(n+1)
        for i in range(2,n+1):
            s = countandsay[i-1]
            j=0
            res = ""
            cur=s[0]
            count=0
            while j<len(s):
                if s[j] == cur:
                    count+=1
                else:
                    res+=str(count)+str(cur)
                    cur = s[j]
                    count=1
                j+=1
            print(res)
            res+=str(count)+str(cur)
            countandsay[i] = res
        return countandsay[-1]