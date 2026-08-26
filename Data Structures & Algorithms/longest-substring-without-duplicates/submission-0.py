class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        deq = deque()
        sub = set()

        max_len = 0
        for i in s:
            while i in sub:
                ele = deq.popleft()
                sub.remove(ele)
            deq.append(i)
            sub.add(i)
            max_len = max(max_len,len(sub))
        return max_len
                

        