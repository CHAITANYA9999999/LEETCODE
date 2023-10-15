class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo={}
        def solve(current,remaining):
            if current<0 or current>=arrLen or current-remaining>0:
                return 0
            elif not (remaining or current):
                return 1
            elif (current,remaining) in memo:
                return memo[(current,remaining)]
            else:
                c=solve(current+1,remaining-1)
                memo[(current+1,remaining-1)]=c
                b=solve(current,remaining-1)
                memo[(current,remaining-1)]=b
                a=solve(current-1,remaining-1)
                memo[(current-1,remaining-1)]=a
                return (a+b+c)%(10**9+7)
        return solve(0,steps)