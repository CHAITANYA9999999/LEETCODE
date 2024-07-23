import bisect
class Solution(object):
    def frequencySort(self, nums):
        freq = collections.Counter(nums)
        freqs = {}
        for num,frequency in freq.items():
            if frequency not in freqs:
                freqs[frequency] = []
            print(num,frequency)
            bisect.insort(freqs[frequency],num)
        res = []
        for frequency in sorted(freqs.keys()):
            for num in reversed(freqs[frequency]):
                res.extend([num]*frequency)
        return res