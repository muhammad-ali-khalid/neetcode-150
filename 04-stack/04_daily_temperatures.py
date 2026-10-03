class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        i = len(temperatures) - 1
        while i >= 0:
            while s and temperatures[i] >= s[-1][0]:
                s.pop()
            if s:
                res[i] = s[-1][1] - i
            s.append((temperatures[i], i))
            i -= 1
        return res