class Solution:
    def count(self, n):
        
        return 2 ** (n * (n-1) // 2)