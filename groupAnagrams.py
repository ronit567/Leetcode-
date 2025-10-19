from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            count = [0] * 26  # for lowercase letters
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # tuples can be dictionary keys
            anagrams[key].append(s)
        
        return list(anagrams.values())
