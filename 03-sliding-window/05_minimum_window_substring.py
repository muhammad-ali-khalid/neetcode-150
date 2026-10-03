class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or s == "" or len(t) > len(s):
            return ""
        h , w_h = {}, {}
        for ch in t:
            h[ch] = 1 + h.get(ch, 0)
        have, need = 0, len(h)
        res = [-1, -1]
        length, min_length = 0, float("inf")
        l, r = 0, 0
        while r < len(s):
            if s[r] in h:
                w_h[s[r]] = 1 + w_h.get(s[r], 0)
                if w_h[s[r]] == h[s[r]]:
                    have += 1
            while have == need and l <= r:
                length = r - l + 1
                if length < min_length:
                    res = [l, r]
                    min_length = length
                if s[l] in w_h:
                    w_h[s[l]] -= 1
                    if w_h[s[l]] < h[s[l]]:
                        have -= 1
                l += 1
            r += 1
        return s[res[0]: res[1] + 1]