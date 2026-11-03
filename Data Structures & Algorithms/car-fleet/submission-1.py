class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        front_car = []
        for i in range(len(position)):
            pair = (position[i], speed[i])
            pairs.append(pair)
        
        pairs.sort(reverse=True)
        for p, s in pairs:
            time = (target - p) / s
            if not front_car or time > front_car[-1]:
                front_car.append(time)
        return len(front_car)

