class Solution(object):
    def minDeletions(self, s):
        a=Counter(s)
        l2=list(a.values())
        i=0
        count=0
        while l2!=set(l2) and i<len(l2):
            if l2.count(l2[i])!=1:
                l2[i]-=1
                count+=1
                if l2[i]==0:
                    l2.remove(0)
            else:
                i+=1
        return count