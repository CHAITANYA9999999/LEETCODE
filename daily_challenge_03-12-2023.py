class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        curr = points[0]
        time=0
        for i in range(1,len(points)):
            time += max(abs(curr[0] - points[i][0]),abs(curr[1] - points[i][1]))
            curr=points[i]
        return time
