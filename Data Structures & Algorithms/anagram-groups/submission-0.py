class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashAnagram(word :str) -> ():
            return ''.join(sorted(word))
        from collections import defaultdict
        g = defaultdict(list)
        for string in strs:
            g[hashAnagram(string)].append(string)
        # print(g)
        return g.values()
            
        