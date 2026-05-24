class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1

        if self.cache.get(n):
            return self.cache.get(n);

        left = self.climbStairs(n-1) if n-1>=0 else 0
        self.cache[n-1] = left
        right = self.climbStairs(n-2) if n-2>=0 else 0
        self.cache[n-2] = right

        self.cache[n] = left + right

        return left + right
        