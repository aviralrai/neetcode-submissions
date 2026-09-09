class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = {}
        for i in range(len(position)):
            car[position[i]] = speed[i]
        sorted_car = dict(sorted(car.items()))

        time = [(target - x)/s for x,s in sorted_car.items()]
        ans = 0
        maxtime = 0
        for ele in reversed(time):
            if ele > maxtime:
                maxtime = ele
                ans += 1
        return ans


        