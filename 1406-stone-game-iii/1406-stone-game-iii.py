class Solution:
    def stoneGameIII(self, values):
        dp = {}

        def dfs(i):
            if i == len(values):
                return 0

            if i in dp:
                return dp[i]

            res = float("-inf")
            total = 0

            for j in range(i, min(i + 3, len(values))):
                total += values[j]
                res = max(res, total - dfs(j + 1))

            dp[i] = res
            return res

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"