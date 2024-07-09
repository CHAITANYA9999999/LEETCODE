class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + [x/1.0 for x in nums] + [-float("inf")]
        l = 1
        r = len(nums)-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid-1
            elif nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return -1