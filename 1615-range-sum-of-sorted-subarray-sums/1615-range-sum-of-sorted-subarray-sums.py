class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sum = []
        MOD = 10**9 + 7
        n = len(nums)

        for i in range(n):
            cur_sum = 0
            for j in range(i,n):
                cur_sum += nums[j]
                subarray_sum.append(cur_sum)

        res = 0
        subarray_sum.sort()
        for i in range(left-1,right):
            res = (res+subarray_sum[i])%MOD
        return res