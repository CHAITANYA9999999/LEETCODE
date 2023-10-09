class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index=0
        left=0
        right=len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                index=1
                break
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
        if not index:
            return [-1,-1]
        left = mid
        right = mid
        while left!=0 and nums[left-1]==target:
            left-=1
        while right!=len(nums)-1 and nums[right+1]==target:
            right+=1
        return [left,right]