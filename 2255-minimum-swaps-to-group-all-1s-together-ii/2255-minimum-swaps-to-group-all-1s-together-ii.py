class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        window = nums.count(1)
        l,r = 1,window
        one_count = nums[0:window].count(1)
        min_swaps = window - one_count
        while l<2*n:
            one_count += nums[r%n] - nums[(l-1)%n]
            min_swaps = min(min_swaps,window - one_count)
            l +=1
            r +=1
        
        return min_swaps