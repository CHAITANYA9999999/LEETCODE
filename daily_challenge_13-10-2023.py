class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def climb(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            one_step_cost = cost[i - 1] + climb(i - 1)
            two_step_cost = cost[i - 2] + climb(i - 2)
            memo[i] = min(one_step_cost, two_step_cost)
            return memo[i]

        return climb(n)