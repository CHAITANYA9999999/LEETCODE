class Solution(object):
    def countOrders(self, n):
        count=1
        for i in range(2,n+1):
            count*=(2*i-1)*i
        return count%(7+10**9)