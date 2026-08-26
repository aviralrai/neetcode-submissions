class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        for i in s1:
            if i in freq_s1.keys():
                freq_s1[i] += 1
            else:
                freq_s1[i] = 1
        n = len(s1)
        # print(freq_s1)
        for i in range(len(s2)- n +1):
            win = s2[i:i+n]
            freq_win = {}
            for j in win:
                if j in freq_win.keys():
                    freq_win[j] += 1
                else:
                    freq_win[j] = 1
            # print(freq_win)
            if freq_win == freq_s1:
                return True
        return False

        