class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        maxi=-1
        while i<len(nums) and nums[i]<0:
            if -nums[i] in nums:
                maxi=max(maxi,abs(nums[i]))
            i+=1
        return maxi