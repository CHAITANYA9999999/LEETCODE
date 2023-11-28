class Solution:
    def numberOfWays(self, corridor: str) -> int:
        a = corridor.count('S')
        if a%2 or not a:
            return 0

        total=1
        s_count=0
        p_count=0
        for i in corridor:
            if s_count!=2:
                if i=='S':
                    s_count+=1
                else:
                    continue
            else:
                if i=='P':
                    p_count+=1
                    continue
                else:
                    total*=(p_count+1)
                    p_count=0
                    s_count=1
            
        return total%(1000000007)
