class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i], (target - position[i]) / speed[i]))
        
        #sort by position, reverted
        cars.sort(key= lambda el: el[0], reverse=True)

        numfleets = 0
        T = 0

        for car in cars:
            #if its arrival time is higher than T, wwe create a new fleet
            #if lower or equal we joing the fleet
            if car[2] > T:
                numfleets += 1
                T = car[2]
            
        return numfleets
        