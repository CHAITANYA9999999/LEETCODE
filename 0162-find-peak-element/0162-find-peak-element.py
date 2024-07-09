class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + [x/1.0 for x in nums] + [-float("inf")]
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i-1