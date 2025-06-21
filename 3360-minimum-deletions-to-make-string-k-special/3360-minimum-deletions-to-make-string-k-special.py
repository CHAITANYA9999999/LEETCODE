class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = collections.Counter(word)
        lis = sorted(list(c.values()))
        min_deletion = len(word)
        left_acc=0
        for i in range(len(lis)):
            thres = lis[i]+k
            deletions = left_acc
            for j in range(i+1,len(lis)):
                if lis[j]>thres:
                    deletions += lis[j] - thres
            min_deletion = min(min_deletion, deletions)
            left_acc+=lis[i]
        return min_deletion