class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]
        sort_d = dict(sorted(d.items()))
        time = []
        for key,val in sort_d.items():
            dist = target - key
            time.append(dist/val)
        for i in range(len(speed)-2,-1,-1):
            if time[i] < time[i+1]:
                time[i] = time[i+1]
        return len(set(time))