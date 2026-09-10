class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        lo, hi = 1, max(piles)
        def ifPossible(mid: int)-> bool:
            c = 0
            for pile in piles:
                c += math.ceil(pile/mid)
                if c > h:
                    return False
            return True
        while lo < hi:
            mid = (lo+hi)//2
            if total > h*mid:
                lo = mid + 1
            elif ifPossible(mid):
                hi = mid
            else: lo = mid + 1
        return lo
        