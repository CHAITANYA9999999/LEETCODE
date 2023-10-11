class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        start = sorted([a for a,b in flowers])
        end = sorted([b for a,b in flowers])
        return [bisect_right(start,i) - bisect_left(end,i) for i in people]