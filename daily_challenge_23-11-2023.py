class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            diff = arr[1] - arr[0]
            cur = True
            for j in range(1,len(arr)-1):
                if arr[j+1]-arr[j]!=diff:
                    cur = False
                    break
            ans.append(cur)
        return ans
