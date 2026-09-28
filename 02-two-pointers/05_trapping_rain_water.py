class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        max_height = 0
        i = 0
        while i < len(height):
            current_height = height[i]
            max_height = max(max_height, current_height)
            left_max[i] = max_height
            i += 1
        max_height = 0
        i = len(height) - 1
        while i >= 0:
            current_height = height[i]
            max_height = max(max_height, current_height)
            right_max[i] = max_height
            i -= 1
        total = 0
        i = 0
        while i < len(height):
            value = min(left_max[i], right_max[i]) - height[i]
            if value > 0:
                total += value
            i += 1
        return total