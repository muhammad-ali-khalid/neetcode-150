class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if self.canFinish(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def canFinish(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours <= h