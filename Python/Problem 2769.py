class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        x = num + t
        for i in range(t):
            if x <= num:
                return x + 1
            else:
                num -= 1
                x += 1
        return x