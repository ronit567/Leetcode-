class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0][:2]
        
        for word in strs:
            if not word.startswith(prefix):
                return ""
        
        return prefix
