import bisect

class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        start = sorted([a for a,b in flowers])
        end = sorted([b for a,b in flowers])
        return [bisect.bisect_right(start,i) - bisect.bisect_left(end,i) for i in people]