class Solution:
    def fib(self, n: int) -> int:
        sol = [0,1]
        for i in range(2, n+1):
            sol.insert(i, sol[i-1] + sol[i-2])
        return sol[n]
