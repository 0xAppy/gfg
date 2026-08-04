class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        return 1 if n == 0 or n == 1 else n*self.factorial(n-1)