class Solution(object):
    def minimumTime(self, n, relations, time):
        dependency=[[] for _ in range(n)]

        for i,j in relations:
            dependency[j-1].append(i-1)

        memo={}
        
        def calcTime(course):
            if course in memo:
                return memo[course]
            
            if dependency[course]==[]:
                memo[course] = time[course]
                return time[course]
            
            max_pre_time = 0
            for pre in dependency[course]:
                max_pre_time = max(max_pre_time,calcTime(pre))
            
            memo[course] = time[course] + max_pre_time
            return memo[course]
            
        min_time=0
        for i in range(n):
            min_time = max(min_time,calcTime(i))
        return min_time