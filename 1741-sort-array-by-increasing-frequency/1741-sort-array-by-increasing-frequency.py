import bisect
class Solution(object):
    def frequencySort(self, nums):
        freq = collections.Counter(nums)
        freqs = {}
        for num,frequency in freq.items():
            if frequency not in freqs:
                freqs[frequency] = []
            print(num,frequency)
            freqs[frequency].append(num)
        res = []
        for frequency in sorted(freqs.keys()):
            for num in sorted(freqs[frequency],reverse = True):
                res.extend([num]*frequency)
        return res