import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r,n = 1, max(piles), len(piles)
        ans = r
        while l<=r:
            mid = (l+r)//2
            hours = 0
            for i in range(n):
                if mid>=piles[i]:
                    hours+=1
                else:
                    hours+=math.ceil(piles[i]/mid)
            if hours<=h:
                ans = mid
                r = mid-1
            elif hours>h:
                l=mid+1
        return ans