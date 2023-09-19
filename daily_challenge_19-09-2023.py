class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in (nums):
            if i not in d:
                d[i]=i
            else:
                return i
        return -1