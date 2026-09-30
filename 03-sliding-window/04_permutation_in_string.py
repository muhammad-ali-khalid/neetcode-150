class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_1 = [0] * 26
        freq_2 = [0] * 26
        for ch in s1:
            freq_1[ord(ch) - ord('a')] += 1
        i = 0
        while i <= len(s2) - len(s1):
            j = i
            while j < i + len(s1):
                freq_2[ord(s2[j]) - ord('a')] += 1
                j += 1
            if freq_1 == freq_2:
                return True
            freq_2 = [0] * 26
            i += 1
        return False