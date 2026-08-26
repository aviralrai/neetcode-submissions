class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element_set = set()
        for ele in nums:
            if ele in element_set:
                return True
            element_set.add(ele)
        return False
         