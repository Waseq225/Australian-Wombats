class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ways = [0] * (n + 1)
            ways[1] = 1
            ways[2] = 2

            for i in range(3, n + 1):
                ways[i] = ways[i - 1] + ways[i - 2] #calculates the number of ways to climb i stairs based on the 
                                                    #solutions for i - 1 and i - 2. It uses dynamic programming to 
                                                    #build up the solution.     

            return ways[n]
