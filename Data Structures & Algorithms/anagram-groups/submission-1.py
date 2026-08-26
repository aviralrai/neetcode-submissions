class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        def hashAnagram(word: str) -> str:
            return ''.join(sorted(word))
        g = defaultdict(list)
        for string in strs:
            g[hashAnagram(string)].append(string)
        return list(g.values())