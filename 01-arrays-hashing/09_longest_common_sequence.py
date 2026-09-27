class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lcs = 1
        s = {n for n in nums}
        for n in nums:
            if n - 1 in s:
                continue
            else:
                ccs = 1
                while n + 1 in s:
                    ccs += 1
                    n += 1
                lcs = max(lcs, ccs)
        return lcs