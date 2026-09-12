class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid  = (lo+hi)//2
            if nums[lo] <= nums[mid]:
                if target <= nums[mid] and target >= nums[lo]:
                    hi = mid
                else:
                    lo = mid+1
            else:
                if target <= nums[hi] and target >= nums[mid]:
                    lo = mid
                else:
                    hi = mid - 1
        return lo if nums[lo] == target else -1

            
        