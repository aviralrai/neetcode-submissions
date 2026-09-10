class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < len(nums) and target == nums[lo] else -1
        