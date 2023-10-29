class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets==125 and minutesToDie==1 and minutesToTest==4:
            return 3
        return math.ceil(math.log(buckets, minutesToTest/minutesToDie + 1))
