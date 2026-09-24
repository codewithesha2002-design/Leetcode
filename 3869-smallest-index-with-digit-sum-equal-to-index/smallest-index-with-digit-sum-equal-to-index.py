class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digital_sum = 0

            while num > 0:
                digital_sum += num % 10
                num //= 10

            if digital_sum == i:
                return i

        return -1