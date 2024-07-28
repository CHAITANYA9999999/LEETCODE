class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def helper(subset,i):
            if i==len(nums):
                self.ans.append(subset)
                return
            helper(subset,i+1)
            helper(subset+[nums[i]],i+1)
        helper([],0)
        return self.ans