class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count , ans , cur = 0 , 0 , nums[0]
        for i in range(1,len(nums)):
            if cur != nums[i] :
                count += 1 
                ans += count 
                cur = nums[i]
            else:
                ans += count 
        return ans 
