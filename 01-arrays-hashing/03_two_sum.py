class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, i in enumerate(nums):
            remaining = target - i
            if remaining in d:
                return [d.get(remaining), index]
            d[i] = index
        return []