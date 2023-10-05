from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        coun = Counter(nums)
        lim = len(nums)//3
        l=[]
        for i in coun:
            if coun[i]>lim:
                l.append(i)

        return l