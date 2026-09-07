class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        end_count = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            end_count[idx] = (sum(end_count) + 1) % MOD
        return sum(end_count) % MOD