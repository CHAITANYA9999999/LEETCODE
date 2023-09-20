class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # def help(nums,count,cur):
        #     if cur==0:
        #         return count
        #     elif cur<0 or  len(nums)==0:
        #         return float('inf')
        #     return min(help(nums[1:],count+1,cur-nums[0]),help(nums[:-1],count+1,cur-nums[-1]))
        # a=help(nums,0,x)
        # if a==float('inf'):
        #     return -1
        # return a
        
        target, n = sum(nums) - x, len(nums)
        
        if target == 0:
            return n
        
        max_len = cur_sum = left = 0
        
        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len else -1