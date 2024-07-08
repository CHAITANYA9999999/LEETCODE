class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(n))
        cur=0
        while len(l)!=1:
            idx = (cur+k-1)%len(l)
            l.pop(idx)
            cur = idx
            x = [i+1 for i in l]
            print(x,cur)
        return l[0]+1