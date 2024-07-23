class Solution(object):
    def productExceptSelf(self, nums):
        product=1
        pwithoutzero=1
        zero=0
        for i in nums:
            if(i!=0):
                pwithoutzero*=i
            else:
                zero+=1
            product*=i
        return [product/x if x!=0 else (pwithoutzero if zero==1 else 0) for x in nums] 