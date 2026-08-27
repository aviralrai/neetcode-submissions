class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hi = len(numbers)-1
        lo = 0
        while hi >= lo:
            if numbers[lo] + numbers[hi] == target:
                return [lo+1,hi+1]
            elif numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                lo +=1

        