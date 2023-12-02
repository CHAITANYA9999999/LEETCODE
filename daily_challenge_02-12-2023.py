from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        good = 0
        c = Counter(chars)
        print(c)
        for word in words:
            counter = Counter(word)
            isGood = True
            for i in counter.keys():
                if i in c and counter[i]<=c[i]:
                    continue
                else:
                    isGood = False
                    break
            if isGood:
                good+=len(word)
        return good
