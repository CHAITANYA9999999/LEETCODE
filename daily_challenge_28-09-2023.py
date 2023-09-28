class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if not i%2:
                l.insert(0,i)
            else:
                l.append(i)
        return l