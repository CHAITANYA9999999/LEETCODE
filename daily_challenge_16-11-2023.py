class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(int(x,2) for x in nums)
        l = len(nums)
        for i in range(2**l):
            if i not in s:
                a=bin(i)[2:]
                return '0'*(l-len(a)) + a
        return ''
