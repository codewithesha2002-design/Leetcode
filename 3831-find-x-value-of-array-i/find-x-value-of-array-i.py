class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k  # dp[r] holds number of subarrays ending at current index with product % k == r
        
        for num in nums:
            v = num % k
            next_dp = [0] * k
            
            # Extend existing subarrays ending at the previous position
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * v) % k] += dp[r]
            
            # Start a new single-element subarray at current position
            next_dp[v] += 1
            
            # Aggregate counts ending at the current index
            for r in range(k):
                ans[r] += next_dp[r]
                
            dp = next_dp
            
        return ans

