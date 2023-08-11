class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= n):
                candies[i]=True
            else:
                candies[i]=False
        return candies