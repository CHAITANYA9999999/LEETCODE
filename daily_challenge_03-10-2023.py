from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        l=Counter(nums)
        count=0
        for i in l.keys():
            if l[i]>1:
                count+=(l[i]*(l[i]-1))/2
        return count