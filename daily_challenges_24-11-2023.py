class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l=0
        r=len(piles)-2
        piles.sort()
        my_coins=0
        while l<r:
            my_coins += piles[r]
            l+=1
            r-=2
        return my_coins
