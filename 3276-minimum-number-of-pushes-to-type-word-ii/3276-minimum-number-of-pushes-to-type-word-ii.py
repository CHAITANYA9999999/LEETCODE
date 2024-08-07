class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        l = sorted(list(c.items()), key = lambda x : (x[1],x[0]), reverse = True)
        cur_press = 1
        presses = 0
        print(list(enumerate(l)))
        for i,ele in list(enumerate(l)):
            presses += ele[1]*cur_press
            cur_press = (i+1)//8 + 1
        return presses