class Solution:

  def totalNumbers(self, digits: list[int]) -> int:
    unique_numbers = set()
    n = len(digits)

    # i = hundreds place, j = tens place, k = units place
    for i in range(n):
      if digits[i] == 0:
        continue  # Hundreds place cannot be zero

      for j in range(n):
        if j == i:
          continue

        for k in range(n):
          if k == i or k == j:
            continue

          # Units place must be even
          if digits[k] % 2 == 0:
            num = digits[i] * 100 + digits[j] * 10 + digits[k]
            unique_numbers.add(num)

    return len(unique_numbers)