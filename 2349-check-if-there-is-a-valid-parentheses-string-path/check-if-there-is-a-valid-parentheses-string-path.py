class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Path length must be even to have balanced parentheses
        if (m + n - 1) % 2 != 0:
            return False
        
        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        # dp[r][c] holds the set of possible open parentheses balances at grid[r][c]
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Starting state
        dp[0][0].add(1)
        
        max_bal = (m + n) // 2
        
        for r in range(m):
            for c in range(n):
                for bal in dp[r][c]:
                    # Try moving Down
                    if r + 1 < m:
                        next_bal = bal + (1 if grid[r + 1][c] == '(' else -1)
                        if 0 <= next_bal <= max_bal:
                            dp[r + 1][c].add(next_bal)
                    
                    # Try moving Right
                    if c + 1 < n:
                        next_bal = bal + (1 if grid[r][c + 1] == '(' else -1)
                        if 0 <= next_bal <= max_bal:
                            dp[r][c + 1].add(next_bal)
                            
        # Check if balance 0 is reachable at the destination cell
        return 0 in dp[m - 1][n - 1]