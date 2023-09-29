class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l=nums[:]
        l.sort()
        return (nums==l or nums==l[::-1])