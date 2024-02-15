class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        default = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            default[key].append(word)
        return default.values()