class Solution(object):
    def minimumReplacement(self, nums):
        upper_bound=nums[-1]
        operations = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=upper_bound:
                upper_bound=nums[i]
            else:
                t=nums[i]//upper_bound
                print(t)
                if nums[i]%upper_bound!=0:
                    t+=1
                operations += t-1
                upper_bound=nums[i]//t
        return operations