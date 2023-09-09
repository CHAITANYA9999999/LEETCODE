class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums=nums+nums[::-1]
        # def solve(nums,target,summ,i,count):
        #     if i>=len(nums)-1:
        #         return 0
        #     if summ >=target:
        #         return 0

            
        #     if nums[i]+solve(nums,target,summ+nums[i],i,count) == target:

        #         count+=1
        #     else:
        #         solve(nums,target,summ,i+1,count)
        #     return count
        # return solve(nums,target,0,0,0,{})
        nums.sort() 
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0
            
            count = 0
            for num in nums:
                if n - num < 0:
                    break 
                count += helper(n - num)
                
            memo[n] = count
            return count
        
        return helper(target)