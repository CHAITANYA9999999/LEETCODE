class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dist[i]/speed[i] for i in range(len(dist))]
        time.sort()
        print(time)
        for i in range(len(dist)):
            if time[i]-i<=0:
                return i
        return i+1
