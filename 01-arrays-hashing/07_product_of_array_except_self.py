class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        suffix = 1
        result.append(1)
        # prefix
        i = 1
        while i < len(nums):
            prefix = prefix * nums[i - 1]
            result.append(prefix)
            i = i + 1
        # suffix
        i = len(nums) - 2
        while i >= 0:
            suffix = suffix * nums[i + 1]
            result[i] = result[i] * suffix
            i = i - 1
        return result