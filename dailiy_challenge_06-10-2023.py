class Solution:
    def integerBreak(self, n: int) -> int:
        d={}
        def help(num):
            if num==1:
                return 1
            if num in d:
                return d[num]
            maxx=num-1
            for i in range(1,num-1):
                a=help(i)
                b=help(num-i)
                maxx=max(maxx,a*b,a*(num-i),i*b,i*(num-i))
            d[num]=maxx
            return maxx
        return help(n)