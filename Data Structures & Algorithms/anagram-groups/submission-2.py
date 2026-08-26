class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)
        for string in strs:
            # act = {a:1,c:1,t:1}
            c = [0] * 26
            for i in string:
                c[ord(i)-ord('a')] += 1
            group[tuple(c)].append(string)
        return list(group.values())