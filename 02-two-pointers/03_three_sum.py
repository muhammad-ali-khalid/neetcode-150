class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) and nums[i] <= 0:
            left = i + 1
            right = len(nums) - 1
            if i == 0 or nums[i] != nums[i - 1]:
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum < 0:
                        left += 1
                    elif sum > 0:
                        right -= 1
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
            i += 1
        return res