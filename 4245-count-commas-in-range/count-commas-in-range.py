class Solution:

    def countCommas(self, n: int) -> int:
        total_commas = 0

        # Numbers from 1,000 to 999,999 have 1 comma
        if n >= 1000:
            total_commas += min(n, 999999) - 1000 + 1

        # Numbers from 1,000,000 to 999,999,999 have 2 commas
        if n >= 1000000:
            total_commas += (min(n, 999999999) - 1000000 + 1) * 2

        # Numbers from 1,000,000,000 onwards have 3 commas
        if n >= 1000000000:
            total_commas += (n - 1000000000 + 1) * 3

        return total_commas