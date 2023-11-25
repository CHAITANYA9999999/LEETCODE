class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        lsum=0
        rsum=sum(nums)
        nums = [0] + nums
        length = len(nums)
        result=[]
        for i in range(1,length):
            lsum+=nums[i-1]
            rsum-=nums[i]
            result.append(nums[i]*(i-1)-lsum + rsum - nums[i]*(length-i-1))

        return result
