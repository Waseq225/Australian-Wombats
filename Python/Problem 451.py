class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = {i: s.count(i) for i in set(s)}
        output = sorted(res, key=lambda x: res[x], reverse=True)
        result = "".join([char * res[char] for char in output])
        return result